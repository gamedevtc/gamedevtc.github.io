# Portfolio assistant worker

The API proxy behind the "Ask Me" section on gamedevtc.github.io.

GitHub Pages is static, so the site cannot call the Claude API directly: an API key in client
JavaScript is visible in view-source and gets scraped. This worker holds the key, validates and
rate limits requests, and streams answers back to the page.

It reads the knowledge base and resume data from the **live site** on a 5 minute cache, so
iterating on what the assistant says is a push to the portfolio repo. You only redeploy this
worker when you change worker code.

---

## Deploy

From this directory:

```bash
npm install

# 1. Log in (opens a browser once)
npx wrangler login

# 2. Store the API key. This is a secret, never a var in wrangler.toml.
npx wrangler secret put ANTHROPIC_API_KEY

# 3. Ship it
npx wrangler deploy
```

Deploy prints a URL like `https://portfolio-assistant.<your-subdomain>.workers.dev`.

Confirm it is alive:

```bash
curl https://portfolio-assistant.<your-subdomain>.workers.dev/health
```

Then paste that base URL into `endpoint` in `assistant.json` at the repo root.

---

## Rate limiting (do this before going public)

Without a KV binding the limiter is inactive and the endpoint is open to anyone who finds it.

```bash
npx wrangler kv namespace create RATE_LIMIT
```

Paste the returned id into `wrangler.toml`, uncomment the `[[kv_namespaces]]` block, then:

```bash
npx wrangler secret put RATE_LIMIT_SALT   # any random string
npx wrangler deploy
```

### The two layers, and what each is actually worth

**Layer 1, `[[ratelimits]]` in `wrangler.toml` (5 per IP per 60s).** Strongly consistent, no write
quota. This is the layer that does real work. It is *permissive* by design: measured against a
limit of 8 it let roughly 16 through before clamping, so treat the effective ceiling as about
double the configured number.

**Layer 2, KV (about 40 per IP per day).** Weak. KV has no atomic increment, so the
read-modify-write loses increments whenever requests overlap. Measured: **20 counted out of ~95
actual**, an undercount of roughly 5x. It counts accurately only when requests are spread out, so
treat it as a soft backstop against slow steady abuse and never as an exact cap.

Both fail **closed** -- if the backend errors, requests are rejected rather than waved through.

### The guarantee neither layer gives you

Rate limiting is per IP, so it does not bound your total bill. Two things do:

1. **A spend limit in the Anthropic console.** This is the only hard ceiling. Set it.
2. **Turnstile** (next section). A script cannot solve it, which removes the automated-abuse case
   that rate limiting only slows down.

If you want a genuinely accurate counter, it needs Durable Objects rather than KV. That is real
added complexity and probably not worth it for a portfolio, given the two controls above.

---

## Turnstile (optional, recommended)

Cloudflare's invisible bot check. Free and unlimited.

1. Create a widget at dash.cloudflare.com -> Turnstile.
2. Put the **site key** in `turnstileSiteKey` in `assistant.json`.
3. Store the **secret key** here: `npx wrangler secret put TURNSTILE_SECRET`

The worker skips verification entirely when `TURNSTILE_SECRET` is unset, so you can add this later
without touching any code.

---

## The two kill switches

They are independent on purpose.

| Switch | Where | Effect |
|---|---|---|
| `enabled` in `assistant.json` | portfolio repo | Hides the section and its nav entry. Visitors see nothing. |
| `ASSISTANT_ENABLED` in `wrangler.toml` | this worker | Endpoint refuses everything with a 503. |

The site one is the normal control: edit, push, done. The worker one is the emergency brake if the
endpoint is ever getting hammered, since it takes effect without waiting on a Pages rebuild.

To pull the endpoint down immediately:

```bash
npx wrangler deploy --var ASSISTANT_ENABLED:false
```

---

## Watching it run

```bash
npx wrangler tail
```

Every completed answer logs its token usage:

```json
{"in":4,"cacheWrite":0,"cacheRead":8600,"out":180}
```

`cacheRead` being large and `cacheWrite` zero is what you want -- it means the ~8.6k token corpus
is being served from cache at 0.1x input price. If `cacheRead` is always 0 across back to back
questions, something is changing the system prompt between requests and caching is not engaging.

---

## Tuning

Everything worth changing is at the top of `src/index.js`:

| Constant | Default | Note |
|---|---|---|
| `MODEL` | `claude-sonnet-5` | `claude-opus-5` costs roughly 2.5x and handles hostile questions more gracefully |
| `MAX_TOKENS` | `800` | Answer length ceiling |
| `MAX_MESSAGE_CHARS` | `600` | Per message; keep in sync with `maxChars` in `assistant.json` |
| `MAX_TURNS` | `16` | 8 visitor + 8 assistant |
| `DAILY_MAX` | `40` | Approximate per IP per day (see the undercount note above) |
| `DAILY_WINDOW_S` | `86400` | 24 hours |

The burst limit lives in `wrangler.toml` under `[ratelimits.simple]`, not in `src/index.js`.

Latency is dominated by `output_config.effort`, currently `low`. Raising it to `medium` makes
answers more considered and noticeably slower to start.

---

## What it costs

At ~8.6k tokens of cached system prompt and ~350 tokens out per answer, on Sonnet 5:

- First question in a visitor's session: ~$0.02 (cache write)
- Each follow-up within 5 minutes: ~$0.005 (cache read)
- A typical 4 question conversation: ~$0.035

Roughly $7/month at 200 conversations. Cloudflare Workers and KV stay inside the free tier at this
volume.
