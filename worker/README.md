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

Current limit: 15 requests per IP per 10 minutes, set at the top of `src/index.js`. The limiter
fails **closed** -- if KV errors, requests are rejected rather than waved through. On a metered
endpoint, refusing service is the cheaper mistake.

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
| `RATE_LIMIT_MAX` | `15` | Per IP per window |
| `RATE_LIMIT_WINDOW_S` | `600` | 10 minutes |

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
