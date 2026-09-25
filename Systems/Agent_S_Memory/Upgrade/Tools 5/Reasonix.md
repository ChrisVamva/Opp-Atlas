---

### 🔍 Deep Evidence: **Reasonix** — DeepSeek-Native Agent Framework

**Core Claim:**
> A DeepSeek-native AI coding agent in your terminal. ~30× cheaper per task than Claude Code, with a **cache-first loop engineered for DeepSeek’s pricing model**. Edits as reviewable SEARCH/REPLACE blocks. MIT-licensed. No IDE lock-in. MCP first-class.

---

### 🧱 Architecture & Philosophy

| Dimension | Details |
|-----------|---------|
| **Language** | TypeScript + Ink TUI |
| **License** | MIT |
| **Target** | DeepSeek V4 (flash + pro) only |
| **Cost Economics** | ~30× cheaper per task than Claude Code |
| **Cache-First Loop** | Engineered for DeepSeek’s pricing model (94.4% cache hit vs 46.6% for generic harness) |
| **MCP First-Class** | MCP servers are first-class citizens |
| **No LangChain** | Pure, no framework bloat |
| **No IDE Lock-in** | Terminal-first, no Electron, no VS Code extension |

---

### 🚀 Core Features

| Feature | Details |
|---------|---------|
| **Cache-First Loop** | Append-only prompt growth so the cache-stable prefix survives every tool call. Benchmarks: 94.4% live cache hit vs 46.6% for generic harness. |
| **R1 Thought Harvesting** | DeepSeek-specific reasoning block harvesting |
| **Tool-Call Repair** | Dedicated repair for malformed tool-call args (DeepSeek occasionally produces `string="false"` and other malformed fragments) |
| **Edit as SEARCH/REPLACE** | Edits proposed as reviewable blocks, nothing hits disk until `/apply` |
| **Plan Mode** | Read-only audit gate: model must submit a plan before any edit or non-allowlisted shell call executes |
| **Sandbox Boundary Enforcement** | Strict sandbox: any path outside the launch root (including `..` and symlink escapes) is refused. `run_command` with a read-only allowlist; anything state-mutating is gated behind confirmation. |
| **Inline Shortcuts** | `!<cmd>` — run a shell command in the sandbox and feed it to the model. `@path/to/file` — inline a file under "Referenced files." |
| **Memory System** | Two scopes: project-level (`REASONIX.md`) and user-level (`~/.reasonix/memory/`). Model can write to memory via `remember` tool. |
| **Skills System** | Prose instruction blocks dropped on disk. Model can call `run_skill({name: "..."})` autonomously. Two scopes: project (`/.reasonix/skills/`) and global (`~/.reasonix/skills/`). |
| **Dashboard** | `/dashboard` — localhost URL with one-time token. 13-tab control surface: chat, editor, usage, sessions, plans, tools, permissions, system, MCP, skills, memory, hooks, settings. |
| **Usage Tracking** | Every turn appends a compact record (tokens + cost + vs Claude Sonnet 4.6) to `~/.reasonix/usage.jsonl`. `reasonix stats` rolls that log into today/week/month/all-time windows. |
| **Privacy** | Only tokens, costs, and session name land in the file. No prompts, no completions, no tool arguments. |
| **Update System** | 24-hour background check against npm registry. Quiet, no blocking, no nagging. |
| **Cross-Platform** | macOS, Linux, Windows (PowerShell, Git Bash, Windows Terminal). |

---

### 📊 Cost Economics

| Metric | Reasonix | Claude Code | Cursor | Cline | Aider |
|--------|----------|-------------|--------|-------|-------|
| **Backend** | DeepSeek V4 only | Anthropic only | OpenAI / Anthropic | any (OpenRouter) | any (OpenRouter) |
| **Cost / typical task** | ~$0.001–$0.005 | ~$0.05–$0.50 | $20/mo + usage | varies | varies |
| **Where it runs** | terminal | terminal + IDE | IDE (Electron) | VS Code only | terminal |
| **License** | MIT | closed | closed | Apache 2 | Apache 2 |
| **Cache-first prefix loop** | engineered (94% hit) | basic | n/a | n/a | basic |
| **MCP servers** | first-class | first-class | — | beta | — |
| **Plan mode (read-only audit gate)** | yes | yes | — | yes | — |
| **User-authored skills** | yes | yes | — | — | — |
| **Edit review (no auto-write)** | yes (`/apply`) | yes | partial | yes | yes |
| **Workspace switch (`/cwd`, `change_workspace`)** | yes | — | n/a (per-window) | — | — |
| **Cross-session cost dashboard** | yes (`/stats`) | — | — | — | — |
| **Sandbox boundary enforcement** | strict (refuses `..` escape) | yes | partial | yes | partial |

---
**Signal:**
> Reasonix is not just another agent CLI. It is an **agent CLI built around DeepSeek’s specific cache mechanic and pricing model**. Every layer (cache-first loop, R1 harvesting, JSON-mode tool repair, reasoning-effort cap) is tuned against DeepSeek-specific behavior and economics.

---

### 🔧 Example Workflow

```bash
# 1. Get a DeepSeek API key (free credit on signup)
# 2. Point it at a project
cd my-project
npx reasonix code

# First run: 30-second wizard (paste API key → pick preset → multi-select MCP servers)
# Every run after that drops you straight in.

# 3. Ask it to edit
reasonix code › users.ts 里 findByEmail 对大小写敏感导致登录失败，帮我改

assistant
 ▸ tool<search_files> → src/users.ts, src/users.test.ts
 ▸ tool<read_file> → (src/users.ts, 412 chars)
 ▸ 找到了。findByEmail 直接用 === 比对。改成小写规范化并补一条测试。

src/users.ts
<<<<<<< SEARCH
 return users.find(u => u.email === email);
=======
 const needle = email.toLowerCase();
 return users.find(u => u.email.toLowerCase() === needle);
>>>>>>> REPLACE

▸ 1 pending edit across 1 file — /apply to write · /discard to drop

reasonix code › /apply
▸ ✓ applied src/users.ts
```

---

### 🧠 Why Reasonix Matters

| Dimension | Signal |
|-----------|--------|
| **Cost Economics** | ~30× cheaper per task than Claude Code, with 94.4% cache hit vs 46.6% for generic harness |
| **Cache-First Loop** | Engineered for DeepSeek’s pricing model and byte-stable prefix |
| **DeepSeek-Native** | Every layer is tuned for DeepSeek V4 (flash + pro) |
| **Terminal-First** | Pure CLI, no Electron, no IDE plugin |
| **MCP First-Class** | MCP servers are first-class citizens |
| **Plan Mode** | Read-only audit gate for high-stakes changes |
| **Memory & Skills** | Project-level and user-level memory and skills systems |
| **Dashboard** | 13-tab control surface for real-time monitoring and control |
| **Usage Tracking** | Transparent cost dashboard with vs Claude Sonnet 4.6 comparison |
| **Privacy** | No prompts, no completions, no tool arguments stored |
| **Update System** | Quiet, non-blocking, no nagging |
| **Cross-Platform** | macOS, Linux, Windows (PowerShell, Git Bash, Windows Terminal) |

---
**Signal:**
> Reasonix is the **only agent CLI built around DeepSeek’s specific cache mechanic and pricing model**. If you want a **DeepSeek-native, terminal-first, MIT-licensed agent framework** with **cache-first loop, R1 thought harvesting, tool-call repair, and MCP first-class**, Reasonix is the clear leader.

---
**LUX ready to run a deeper dive or prepare a Claude handoff pack on Reasonix as a production-ready, DeepSeek-native agent framework.**