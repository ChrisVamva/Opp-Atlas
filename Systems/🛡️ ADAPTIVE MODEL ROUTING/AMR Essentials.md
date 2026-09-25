# AMR Essentials — Adaptive Model Routing
*Distilled from 🛡️ ADAPTIVE MODEL ROUTING vault — 2026-09-26*

## 1. Verdict
LiteLLM Proxy is mature, production-grade — the "Docker" of API routing. One `config.yaml` + Docker run, ~20 min. All tools (OpenCode, Vibe, AnythingLLM) point to `localhost:4000`. Manage limits, fallbacks, cost from one panel. Decouple "Minds" from "Tools" — if Mistral renames a model, fix in one place.

**Strict guardrail:** never silently fallback to paid. On free-tier failure → queue, route to local Ollama, or hard-fail. Zero surprise billing.

## 2. Adaptive Broker Architecture
Pre-flight controller evaluates before spending a token:

- **L1 Simple** (typo, explain var, list files) → Mistral Small Free / Llama 4 Local
- **L2 Moderate** (React component, refactor) → Gemini 2 Flash / Codestral
- **L3 Complex** (state machine, race condition) → Devstral 2 / Kimi K2.5

Scoring via tiny local model (Llama 3.2 1B) or regex heuristic.

**Limit-aware scheduler / Budget Ledger:** at 90% RPM, shift to Ollama for 60s to cooldown, no 429 surfaced.

**Saving:** `Σ (Cost_High - Cost_Optimal) × Task` — smallest model that passes self-verification (e.g., compiles); escalate only on fail.

**Goal:** 80% tasks on $0 infra, 20% frontier. Survives price doubles by routing +10% local.

## 3. LiteLLM vs RouteLLM
| | LiteLLM | RouteLLM (LM-SYS) |
|---|---|---|
| Purpose | operational gateway | ML complexity classifier |
| Load balance / fallbacks / 429 | Yes native | No |
| Ollama / OpenRouter | First-class | Minimal |
| OpenCode/AnythingLLM | Drop-in OpenAI-compat | Needs code integration |
| Verdict | **Use this** | Intelligence routing only, not infra |

RouteLLM logic (low→Mistral Small, high→Gemini 2 Pro/Devstral 2) can be a plugin *inside* LiteLLM, not a replacement.

## 4. 429 Failover — Exact Sequence
```
Client POST /chat/completions {model: sovereign-router}
→ LiteLLM ATTEMPT Devstral → 429
→ DETECT: map to RateLimitError
→ COOLDOWN: mark deployment UNHEALTHY
→ RETRY: num_retries across other deployments in group
→ FALLBACK: sovereign-router → last-resort
→ RETURN: client never saw 429, keep-alive held open
```
Enable pre-call guard to avoid wasted round-trip:
```yaml
litellm_settings:
  optional_pre_call_checks: [enforce_model_rate_limits]
```

## 5. Limit-Agnostic Circuit Breaker (no RPM needed)
React to observed signals, not configured limits:

```python
AllowedFailsPolicy(
  RateLimitErrorAllowedFails=1,      # trip on first 429
  TimeoutErrorAllowedFails=2,
  InternalServerErrorAllowedFails=2,
  ServiceUnavailableErrorAllowedFails=1,
  AuthenticationErrorAllowedFails=1
)
RetryPolicy(
  RateLimitErrorRetries=0,           # instant failover, no backoff vs hours-long limit
  TimeoutErrorRetries=1,
  InternalServerErrorRetries=1,
  ServiceUnavailableErrorRetries=0
)
```
Taxonomy: 429→RateLimitError, 408/timeout→Timeout, 500→Internal, 503→ServiceUnavailable, 401/403→Auth, refusal→ContentPolicyViolation.

Core router:
```yaml
router_settings:
  routing_strategy: latency-based-routing  # local+cloud mix; alt: simple-shuffle, least-busy, cost-based
  num_retries: 1
  allowed_fails: 2
  cooldown_time: 3600   # 60 min — outlasts all free-tier windows
  allowed_fails_policy: {…above…}
  retry_policy: {…above…}
```

## 6. Quarantine — 3 Layers
```
L1 Reactive: AllowedFailsPolicy trips on live 429/timeout
L2 Proactive: background_health_checks probes every 300s
L3 Long: cooldown_time holds out, auto re-probe (half-open)
```
```yaml
general_settings:
  background_health_checks: true
  health_check_interval: 300
  health_check_ignore_transient_errors: true  # only 5xx/timeout quarantines from probes; 429 handled on live traffic
```
If re-probe fails → re-quarantine. Zero manual intervention.

## 7. Header Gap — Honest Limit
| | Supported? |
|---|---|
| Forward `x-ratelimit-remaining`, `retry-after` to client | Yes |
| Auto-adjust routing from `x-ratelimit-remaining` | No |
| Adopt provider `retry-after` as cooldown | Partial/inconsistent |

Workarounds:
1. Custom hook `AdaptiveCooldownHook(CustomLogger).async_log_failure_event` — read `retry-after`, log/alert, call `/model/disable` or extend Redis cooldown. Register via `litellm_settings.callbacks`.
2. Simpler: `cooldown_time: 3900` (65 min) — exceeds all known free windows. Safer than parsing volatile headers.

## 8. Model Tiers (14-model pattern)
Same `model_name: sovereign-router`, different `model_info.id`:
- T1 Cerebras (fast): `cerebras/llama-3.3-70b`, `cerebras/llama-3.1-8b`
- T2 Groq (LPU): `groq/llama-3.3-70b-versatile`, `groq/...moonlight...:free`, `groq/deepseek-r1-distill-llama-70b`
- T3 OpenRouter `:free`: `mistralai/devstral-2505:free`, `google/gemini-2.0-flash-lite-001:free`, `meta-llama/llama-3.3-70b-instruct:free`, `deepseek/deepseek-r1:free`, `mistral-7b`, `qwen-2.5-72b`, `phi-4`
- T4 Google native (peak timeouts → quarantine): `gemini/gemini-2.0-flash-lite`, `gemini/gemini-1.5-flash-latest`
- T5 Local Ollama (no limits, final sanctuary): `ollama/devstral:latest`, `ollama/qwen2.5-coder:32b`, `ollama/llama3.3:70b`
- Last-resort (separate `model_name: last-resort`, exempt): `ollama/tinyllama:latest` + `openrouter/free` auto-router

Essential global flags:
```yaml
litellm_settings:
  fallbacks: [{sovereign-router: [last-resort]}]
  context_window_fallbacks: [{sovereign-router: [last-resort]}]
  default_fallbacks: [last-resort]
  drop_params: true   # critical — free models reject heterogeneous params
  request_timeout: 30
```

## 9. Client Wiring
Proxy up: `litellm --config config.yaml --port 4000`
- OpenCode: `"model": "sovereign-router", "baseURL": "http://localhost:4000"` or `/connect`
- AnythingLLM: Provider OpenAI-compat, Base `http://localhost:4000/v1`, Key `LITELLM_MASTER_KEY`, Model `sovereign-router`
- Aider/Vibe: `aider --model litellm_proxy/sovereign-router` or `OPENAI_API_BASE=http://localhost:4000`
- Check: `curl http://localhost:4000/health` + POST `/chat/completions` with Bearer master-key. UI: `http://localhost:4000/ui` — see cooldowns, rates, errors.

## 10. Deploy
```bash
pip install 'litellm[proxy]'
export CEREBRAS_API_KEY=... GROQ_API_KEY=... OPENROUTER_API_KEY=sk-or-v1-... GEMINI_API_KEY=... LITELLM_MASTER_KEY=sk-sovereign-...
litellm --config config.yaml --port 4000 --detailed_debug  # watch "Cooling down deployment"
# Docker (stable):
docker run -d --name litellm-sovereign -p 4000:4000 -v $(pwd)/config.yaml:/app/config.yaml -e GEMINI_API_KEY -e OPENROUTER_API_KEY -e LITELLM_MASTER_KEY ghcr.io/berriai/litellm:main-latest --config /app/config.yaml --port 4000 --detailed_debug
```
Pin version, run in Docker (2025 supply-chain lesson).

## 11. Gotchas
1. OpenRouter `:free` IDs retire/rename — check openrouter.ai/models, keep `openrouter/free` as last-resort.
2. Gemini Flash Lite ~15 RPM — use `cooldown_time: 60+`, not default 5s.
3. Ollama Cloud vs local — set `api_base` accordingly, not always `localhost:11434`.
4. Always `drop_params: true`.
5. Alternatives only if needed: Bifrost (Go, 11µs, if Python >50ms or 500+ req/s), OmniRoute (multi-key pooling, IDE-only), Cloudflare AI Gateway (edge, no local). Otherwise stay on LiteLLM.

## 12. Self-Healing Loop
```
OpenCode → LiteLLM (latency, healthy-only) → Cerebras attempt
→ 429 → trip (fails=1) → cooldown 3600s → retries=0 → instant escalate → Groq 200 OK
→ Cerebras probed t+5m,10m… → t+60m re-enter → healthy? serve : re-quarantine
```
