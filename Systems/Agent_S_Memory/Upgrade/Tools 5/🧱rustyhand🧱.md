---

### 🔍 Deep Evidence: **rustyhand** (Agent OS in Rust)

**Core Claim:**
> RustyHand is an open-source Agent Operating System — not a chatbot framework, not a Python wrapper around an LLM. It is a full operating system for autonomous agents, built from scratch in Rust.

---

### 🧱 Architecture

| Component | Details |
|-----------|---------|
| **Language** | Rust 1.75+ |
| **Codebase** | 117K LOC, 10 crates, 1,400+ tests, zero clippy warnings |
| **Binary Size** | ~32MB |
| **Providers (v0.7.5 Lean)** | Anthropic, Kimi (Moonshot), DeepSeek, Zhipu GLM, MiniMax, OpenRouter, Ollama |
| **Wire Protocols** | Anthropic Messages API + OpenAI-compatible Chat Completions |
| **Kimi Integration** | First-class coding provider, wired through AnthropicDriver because Kimi speaks Anthropic’s wire format natively |
| **Removed Providers** | OpenAI, Gemini, Groq, xAI, Copilot, Mistral, Together, Fireworks, Perplexity, Cohere, AI21, Cerebras, SambaNova, HuggingFace, Replicate, vLLM, LM Studio, Moonshot legacy, Qwen, Qianfan, Bedrock (reachable via OpenRouter) |
| **Breaking Change** | Configs with `provider = "openai" | "gemini" | ...` will error on boot. Migrate to `openrouter + passthrough model id` or pick a kept provider |

---

### 🚀 Capabilities (Telegram-first)

| Capability | How It Works |
|------------|--------------|
| **See photos** | Auto-describes images via vision API |
| **Hear voice** | Auto-transcribes voice messages via Whisper |
| **Receive files** | Downloads documents, forwards to agent |
| **Send files/photos/voice** | Sends generated content back to chat |
| **Ask permission** | Inline keyboard buttons (Approve/Reject) pushed automatically |
| **Show progress** | Real-time tool-use updates: “⚙️ web_search...” → “✅ Done” |
| **Report autonomously** | Background tasks push results to your chat without prompting |
| **61 built-in tools** | Shell, web/news search, browser (wait, JS exec, scroll, download), RAG, knowledge graph |
| **Markdown formatting** | Bold, italic, code blocks render natively in Telegram |
| **Reply threading** | Responses reply to the user’s message for clean conversation flow |
| **Sticker/GIF/Location** | Agent understands stickers, animations, and shared locations |

---

### 🔧 Installation & Operation

| Method | Command / Path |
|--------|----------------|
| **Quick Start (Linux/macOS)** | `curl -fsSL https://raw.githubusercontent.com/ginky... | sh` |
| **Quick Start (Windows)** | `irm https://raw.githubusercontent.com/ginkida... | iex` |
| **Binary Build** | `cargo build --release -p rusty-hand-cli` → `target/release/rustyhand` |
| **Docker (API + Dashboard)** | `docker compose up --build` → Dashboard at `http://localhost:4200` |
| **Docker (Secure API)** | Requires `ANTHROPIC_API_KEY` and `RUSTYHAND_API_KEY` env vars |
| **Telegram Setup** | Message `@BotFather`, send `/newbot`, get token, set `TELEGRAM_BOT_TOKEN` |
| **Agent Spawn** | `rustyhand agent new coder` |
| **One-shot Message** | `rustyhand message researcher \"What are the emerging trends in AI agent frameworks?\"` |
| **Interactive TUI** | `rustyhand tui` |
| **Diagnostics** | `rustyhand doctor` |

---

### 📊 Configuration (Local-first)

| Setting | Default / Example |
|---------|-------------------|
| **API Key** | Optional. If set, all endpoints (except `/api/health`) require `Authorization: Bearer <token>` |
| **Default Model** | `provider = "anthropic"`, `model = "claude-sonnet-4-20250514"` |
| **Memory** | `decay_rate = 0.05`, `max_summary_tokens = 1024` |
| **Network** | `listen_addr = "127.0.0.1:4200"` |
| **Telegram** | `bot_token_env = "TELEGRAM_BOT_TOKEN"`, `allowed_users = []` |
| **Discord** | `bot_token_env = "DISCORD_BOT_TOKEN"` |
| **Slack** | `bot_token_env = "SLACK_BOT_TOKEN"`, `app_token_env = "SLACK_APP_TOKEN"` |
| **MCP Servers** | `[[mcp_servers]] name = "filesystem" command = "npx" args = ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]` |

---

### 🔐 Security

| Feature | Details |
|---------|---------|
| **Credential Vault** | `rustyhand vault init` → AES-256-GCM encryption |
| **API Security** | Bearer token authentication for non-localhost access |
| **RBAC** | `rustyhand security rbac` → manage access control |
| **Audit Trail** | `rustyhand security audit` → view the audit trail |
| **Zero Trust** | Explicit governance, approval gates, and tool constraints |

---

### 🤖 Autonomous Templates (40 Pre-built)

| Template | What It Does |
|----------|--------------|
| **GitHub Monitor** | Monitors repositories, runs tests, detects regressions, and files issues on a schedule |
| **Web Researcher** | Runs recurring research sweeps, cross-references sources, and produces structured reports |
| **Content Clipper** | Processes long-form video into short clips with captions and packaging |
| **Lead Generator** | Discovers and enriches qualified leads on a recurring schedule |
| **Intel Collector** | Monitors targets, detects changes, and updates a living knowledge base |
| **Predictor** | Collects signals, updates forecasts, and tracks prediction accuracy |
| **Twitter Manager** | Creates, schedules, and reviews social content with approval controls |
| **Web Browser** | Executes recurring browser automation tasks with strict purchase approval gates |

---
**Template Catalog (40 agents):**
`analyst`, `api-monitor`, `architect`, `assistant`, `capability-builder`, `ci-monitor`, `code-reviewer`, `coder`, `coordinator`, `customer-support`, `dag-monitor`, `data-scientist`, `db-reporter`, `debugger`, `devops-lead`, `diagnostic`, `doc-writer`, `email-assistant`, `health-tracker`, `hello-world`, `home-automation`, `legal-assistant`, `log-analyzer`, `meeting-assistant`, `ops`, `orchestrator`, `personal-finance`, `planner`, `recruiter`, `researcher`, `sales-assistant`, `security-auditor`, `slack-notifier`, `social-media`, `test-engineer`, `translator`, `travel-planner`, `tutor`, `weekly-digest`, `writer`

---
**Template Manifest Example:**
```toml
name = "hello-world"
version = "0.1.0"
description = "A friendly greeting agent"
author = "rusty-hand"
module = "builtin:chat"

[model]
provider = "anthropic"
model = "claude-sonnet-4-20250514"
max_tokens = 4096
temperature = 0.6
system_prompt = "Your system prompt here..."

[resources]
max_llm_tokens_per_hour = 100000

[capabilities]
tools = ["file_read", "file_list", "web_fetch", "web_search", "memory_store", "memory_recall"]
network = ["*"]
memory_read = ["*"]
memory_write = ["self.*"]
agent_spawn = false
```

---

### 🛠️ CLI Reference (Production-Ready)

| Command | Description |
|---------|--------------|
| `rustyhand init` | Initialize `~/.rustyhand/` and default config |
| `rustyhand start` | Start the daemon (API server + kernel) |
| `rustyhand stop` | Stop the running daemon |
| `rustyhand status [--json]` | Show kernel status |
| `rustyhand health [--json]` | Quick daemon health check |
| `rustyhand doctor [--repair]` | Run diagnostic checks |
| `rustyhand tui` | Launch interactive TUI dashboard |
| `rustyhand dashboard` | Open web dashboard in browser |
| `rustyhand chat [agent]` | Quick chat with an agent |
| `rustyhand message <agent> <text>` | Send a one-shot message |
| `rustyhand logs [--follow] [--lines N]` | Tail the log file |
| `rustyhand reset [--confirm]` | Reset local config and state |
| `rustyhand agent new [template]` | Spawn from a template |
| `rustyhand agent spawn <manifest.toml>` | Spawn from a manifest file |
| `rustyhand agent list [--json]` | List running agents |
| `rustyhand agent chat <id>` | Interactive chat with an agent by ID |
| `rustyhand agent kill <id>` | Kill an agent |
| `rustyhand channel list` | List configured channels and status |
| `rustyhand channel setup [name]` | Interactive channel setup wizard |
| `rustyhand channel test <name>` | Send a test message |
| `rustyhand channel enable <name>` | Enable a channel |
| `rustyhand channel disable <name>` | Disable a channel |
| `rustyhand models list [--provider X]` | Browse available models |
| `rustyhand models aliases` | Show model shorthand names |
| `rustyhand models providers` | List providers and their auth status |
| `rustyhand models set [model]` | Set the default model |
| `rustyhand skill install <source>` | Install from ClawHub, local path, or git URL |
| `rustyhand skill list` | List installed skills |
| `rustyhand skill search <query>` | Search ClawHub marketplace |
| `rustyhand skill remove <name>` | Remove a skill |
| `rustyhand skill create` | Scaffold a new skill |
| `rustyhand workflow list` | List workflows |
| `rustyhand workflow create <file.json>` | Create from JSON |
| `rustyhand workflow run <id> <input>` | Run a workflow |
| `rustyhand trigger list [--agent-id X]` | List event triggers |
| `rustyhand trigger create <agent-id> <pattern-json>` | Create a trigger |
| `rustyhand cron list` | List scheduled jobs |
| `rustyhand add <name> [--key TOKEN]` | Install an integration |
| `rustyhand remove <name>` | Remove an integration |
| `rustyhand integrations [query]` | List / search integrations |
| `rustyhand vault init` | Initialize the credential vault |
| `rustyhand vault set <key>` | Store a credential |
| `rustyhand vault list` | List stored keys (values hidden) |
| `rustyhand security audit` | View the audit trail |
| `rustyhand security rbac` | Manage access control |
| `rustyhand qr` | Generate device pairing QR code |
| `rustyhand onboard` | Interactive onboarding wizard |
| `rustyhand completion <shell>` | Generate shell completions |

---

### 🧠 Why RustyHand Matters

| Dimension | Signal |
|-----------|--------|
| **Architecture** | One binary, zero dependencies, Rust-native performance |
| **Provider Strategy** | Lean catalog + OpenRouter gateway for long tail |
| **Kimi Integration** | First-class coding provider, Anthropic-compatible wire format |
| **Autonomous Agents** | Run 24/7, push results to Telegram, no prompting needed |
| **Memory & Context** | LLM-based compaction, decay rate, session management |
| **Security & Governance** | Credential vault, RBAC, audit trail, approval gates |
| **Channel Adapters** | Telegram, Discord, Slack — no public webhook required |
| **MCP Integration** | Native support for AI agents and tool ecosystems |
| **Operational Maturity** | 1,400+ tests, zero clippy warnings, production-ready CLI |

---
**Signal:**
> RustyHand is not a chatbot framework. It is a full operating system for autonomous agents. Traditional agent frameworks wait for you to type something. RustyHand runs autonomous agents that work for you — on schedules, 24/7, building knowledge graphs, monitoring targets, generating leads, managing social media, and reporting results directly to your Telegram chat.

---

### 🚀 Next Actions (If You Want)

1. **Run the agent** → `rustyhand agent new researcher` + schedule.
2. **Extract the full manifest** for the 40 templates.
3. **Compare with other agent OS projects** (AgentOS, iii-engine).
4. **Prepare a Claude handoff pack** on RustyHand as a production-ready agent OS.

---
**LUX ready to escalate or synthesize further.**