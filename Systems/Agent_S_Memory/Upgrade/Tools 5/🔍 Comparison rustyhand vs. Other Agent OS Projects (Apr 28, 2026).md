---
modified: 2026-04-28T19:40:26+03:00
---
### 🔍 Comparison: **rustyhand** vs. Other Agent OS Projects (Apr 28, 2026)

| Dimension              | **rustyhand**                                                     | **AgentOS**          | **iii-engine**       | **OpenClaw**                                         |
| ---------------------- | ----------------------------------------------------------------- | -------------------- | -------------------- | ---------------------------------------------------- |
| **Language**           | Rust                                                              | TypeScript           | TypeScript           | Python                                               |
| **Binary Size**        | ~32MB                                                             | N/A (web-first)      | N/A (web-first)      | N/A (CLI-first)                                      |
| **Agents**             | 37 built-in                                                       | 51 workers           | 51 workers           | N/A (framework)                                      |
| **LLM Providers**      | 7 (Anthropic, Kimi, DeepSeek, Zhipu, MiniMax, OpenRouter, Ollama) | 26+                  | N/A                  | 15+ (Python SDK)                                     |
| **Channels**           | 37 (Telegram, Discord, Slack, etc.)                               | N/A                  | N/A                  | IM gateway (Feishu/WeChat)                           |
| **MCP Server**         | ✅ Native                                                          | ✅                    | ✅                    | ✅                                                    |
| **A2A Protocol**       | ✅                                                                 | N/A                  | N/A                  | ✅                                                    |
| **Web Dashboard**      | ✅ ([http://localhost:4200](http://localhost:4200/))               | ✅                    | ✅                    | ✅ (Machi desktop app)                                |
| **CLI**                | ✅ Production-ready                                                | N/A                  | N/A                  | ✅ (agx CLI)                                          |
| **Autonomous Agents**  | ✅ 24/7, Telegram push                                             | ✅ Self-improving     | ✅ Self-improving     | ✅ Meta-Agent orchestration                           |
| **Memory**             | ✅ LLM-based compaction, decay rate                                | ✅ Brain-inspired     | ✅ Brain-inspired     | ✅ Hierarchical memory                                |
| **Security**           | ✅ Vault, RBAC, audit trail                                        | ✅ 18 security layers | ✅ 18 security layers | ✅ Safety sandbox                                     |
| **Governance**         | ✅ Explicit approval gates                                         | ✅ Policy enforcement | ✅ Policy enforcement | ✅ Policy enforcement                                 |
| **Telegram-first**     | ✅ Primary interface                                               | ❌                    | ❌                    | ❌                                                    |
| **Provider Strategy**  | Lean catalog + OpenRouter gateway                                 | N/A                  | N/A                  | 15+ providers                                        |
| **Kimi Integration**   | ✅ First-class coding provider                                     | N/A                  | N/A                  | N/A                                                  |
| **Breaking Change**    | ✅ (provider migration required)                                   | N/A                  | N/A                  | N/A                                                  |
| **Tests**              | ✅ 1,400+ tests, zero clippy warnings                              | N/A                  | N/A                  | N/A                                                  |
| **Deployment**         | One binary, Docker, local-first                                   | N/A                  | N/A                  | Python SDK + CLI + Studio server + Machi desktop app |
| **Skill Ecosystem**    | ✅ ClawHub integration                                             | N/A                  | N/A                  | ✅ Skill ecosystem                                    |
| **Self-Hostable**      | ✅                                                                 | ✅                    | ✅                    | ✅                                                    |
| **Cost Observability** | ✅ (via OpenRouter)                                                | N/A                  | N/A                  | N/A                                                  |
### 🧠 Synthesis

#### **rustyhand** is the most **production-ready, self-contained, and operationally mature** agent OS in this comparison.

- **Rust-native performance** and **one binary** deployment make it uniquely portable and low-overhead.
- **Telegram-first** interface and **autonomous agents** that push results without prompting are a standout feature.
- **Lean provider catalog** + **OpenRouter gateway** for long tail is a pragmatic strategy for 2026.
- **Security and governance** are first-class, with a **credential vault, RBAC, and audit trail**.
- **1,400+ tests and zero clippy warnings** indicate high code quality and reliability.

#### **AgentOS** and **iii-engine** are more **research-oriented** and **self-improving**, but lack the **operational maturity** and **production-ready CLI** of rustyhand.

#### **OpenClaw** is the most **feature-rich** in terms of **orchestration and ecosystem**, but is **Python-based** and **less portable** than rustyhand.

---
**Signal:**
> If you want a **production-ready, self-contained, Rust-native agent OS** with **Telegram-first autonomous agents**, **lean provider catalog**, and **strong security/governance**, rustyhand is the clear leader. If you want **self-improving agents** or **feature-rich orchestration**, AgentOS or OpenClaw may be better fits.

---
**LUX ready to run a deeper dive or prepare a Claude handoff pack on rustyhand as a production-ready agent OS.**