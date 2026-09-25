# Skills Vault

> A beginner-friendly course collection. **16 skills**, each with a self-contained `First Lesson.md` and a graded `Test1.md`. Lessons are cross-linked so they form a learning path — not a loose folder dump.

**Why this exists:** to turn scattered notes into a coherent course you can start, track, and grow.

---

## Start here (2 minutes)

| If you... | Start with |
|---|---|
| Are new to tech | **Foundations** → Terminal, then work down |
| Already code | Pick your track below; prerequisites are noted in each lesson |
| Just want one skill | Go straight to the folder; every lesson stands alone |

> **Recommended order within a track:** the order listed below. Cross-links (e.g. Python ↔ Terminal ↔ APIs) confirm prerequisites.

---

## Track 1 — Foundations

| Skill | First session | What it teaches |
|---|---|---|
| [Terminal](Terminal/First%20Lesson.md) | Shell basics (`pwd`, `ls`, `cd`, `mkdir`) | Navigate without the file explorer |
| [Keyboard](Keyboard/First%20Lesson.md) | Touch typing: posture, home row, WPM test | Speed and accuracy |
| [Python](Python/First%20Lesson.md) | Install, REPL, variables, first script | Your first programming language |
| [JavaScript](JavaScript/First%20Lesson.md) | Browser console, variables, functions | Browser scripting |

---

## Track 2 — Web & DevOps

| Skill | First session | What it teaches |
|---|---|---|
| [APIs](APIs/First%20Lesson.md) | JSON, GET requests, public APIs | Speak to the internet |
| [Web Design](Web%20Design/First%20Lesson.md) | Layout, typography, color, wireframe | Design a first page |
| [WSL](WSL/First%20Lesson.md) | Ubuntu on Windows, first commands | Windows ↔ Linux interop |
| [CI-CD](CI-CD/First%20Lesson.md) | Pipelines, GitHub Actions workflow | Automate on push |

---

## Track 3 — Automation & Knowledge

| Skill | First session | What it teaches |
|---|---|---|
| [n8n](n8n/First%20Lesson.md) | Workflow automation, two-node workflow | Build automations |
| [Notion](Notion/First%20Lesson.md) | Blocks, pages, databases, dashboard | Personal knowledge base |
| [vector databases](vector%20databases/First%20Lesson.md) | Embeddings (intuition), free playground | Search by meaning |

---

## Track 4 — Business & Content

| Skill | First session | What it teaches |
|---|---|---|
| [Content Creation](Content%20Creation/First%20Lesson.md) | Find an idea, structure, ship one piece | Write and publish |
| [SEO](SEO/First%20Lesson.md) | Search engines, keywords, meta | Rank a first page |
| [product creator](product%20creator/First%20Lesson.md) | Choose idea, outline minimal version | Build your first digital product |
| [product-marketing skills](product-marketing%20skills/First%20Lesson.md) | Audience, positioning, pitch | Write your first headline |
| [service-communication skills](service-communication%20skills/First%20Lesson.md) | Tone, empathy, structure | Rewrite a customer reply |

---

## How every lesson works

Every skill folder has the same two files:

- `First Lesson.md` — ~90 min, beginner-facing, 9-part structure (welcome → prerequisites → roadmap → core concepts → hands-on → cheat sheet → mistakes → quiz → homework / next)
- `Test1.md` — 35-minute graded test (50 pts, 5 parts: concept / fill gaps / hands-on / diagnose / extend) with answer key at bottom

Lessons are written to stand alone. If you want the full path, read left-to-right through your track. If you want just APIs, open `APIs/First Lesson.md`.

---

## Lesson 2 backlog (dead-end promises — being closed)

Every `First Lesson.md` promises a Lesson 2 and homework. This table tracks what's promised vs. delivered. **Status:** audit first; write next.

| Skill | Promised (from lesson / Plan.md) | Status |
|---|---|---|
| Terminal | `if` decisions, loops, lists — decision-making | Pending |
| Keyboard | (follow-up drill routine, speed benchmarks) | Pending |
| Python | `if` / `for` / lists — making choices | Pending |
| JavaScript | Interactivity, events, first interactive page | Pending |
| APIs | POST/PUT, error handling, authentication | Pending |
| Web Design | Responsive layout, typography system | Pending |
| WSL | File interop, package installs, scripting | Pending |
| CI-CD | Multi-step pipeline, secrets, environments | Pending |
| n8n | More nodes, branching, scheduling | Pending |
| Notion | Relations, formulas, automation | Pending |
| vector databases | Real embeddings, cosine similarity | Pending |
| Content Creation | Distribution, editing, promotion | Pending |
| SEO | Keywords, backlinks, analytics | Pending |
| product creator | MVP build, first sales | Pending |
| product-marketing skills | Landing page, email, growth loop | Pending |
| service-communication skills | Escalation, templates, tone guild | Pending |

> **Next: write the first two.** Start with **Terminal** and **Python** (Foundations-first, per track order).

---

## File conventions (no separate CONVENTIONS.md — folded here)

- **Folder names:** keep as-is for now; naming consistency deferred (renames break ~50 links)
- **Lessons / tests:** `First Lesson.md` and `Test1.md`; mirroring for Lesson 2 / Test 2 would be `Lesson 2.md` + `Test2.md`
- **Cross-links:** use relative links (`../Python/First%20Lesson.md`) so they survive folder moves
- **Frontmatter:** deferred ~2 weeks after usage reveals which fields matter (see `proposition.md` §3 for schema)
- **New skills:** copy `New Skill Scaffold.md` from `_Templates/` (when built); otherwise mirror `First Lesson.md` + `Test1.md`

---

## How this vault relates to other files

- [`Plan.md`](Plan.md) — original mission doc for creating the 16 First Lessons + 16 Tests (completed 2026-09-24); stay for context but don't edit today
- [`proposition.md`](proposition.md) — the improvement plan (this is the applied version of it)
- `Notion/Notion export.md` — workspace-migration note; intentionally untouched
- `.freebuff/project-id` — workspace identifier; untouched

---

## Quick links

- **All folders:** list of 16 at root (see tree above by track — folders are flat, not nested)
- **Cross-link check:** every lesson's "Where this meets" / prerequisites points to an existing file
- **Progress tracking:** manual for now (status fields deferred ~2 weeks); no scores recorded until you take tests
- **Question / issue:** open `Plan.md` or `proposition.md` for context; for the vault itself, edit this README so the answer lives at the entry point
