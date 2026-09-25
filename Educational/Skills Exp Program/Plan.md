# Plan — "First Lesson" for Every Skill Folder

> **Mission:** Give every skill folder in this repository a self-contained **First Lesson.md** — a first session written for a complete beginner, deliverable in one sitting today.

---

## 1. Investigation findings (as of mission start)

- **16 skill folders** at the repository root:
  APIs, CI-CD, Content Creation, JavaScript, Keyboard, n8n, Notion, product creator, product-marketing skills, Python, SEO, service-communication skills, Terminal, vector databases, Web Design, WSL
- **15 folders were empty.** **Notion** contained only `Notion export.md` (a workspace-migration note — intentionally left untouched).
- No pre-existing templates, lesson files, or conventions were found, so a single consistent template was defined for all lessons.

---

## 2. Scope decisions (confirmed with the owner)

| Question | Decision |
|---|---|
| Notion folder is not empty — include it? | ✅ Yes, add a First Lesson there too (all **16** folders get one) |
| What does "Keyboard" mean? | **Touch typing** (typing technique, speed, accuracy) |
| What does "service-communication skills" mean? | **Customer-service communication** (writing clear, empathetic replies to users/customers) |

---

## 3. The shared lesson template

Every `First Lesson.md` follows the same 9-part structure so the collection feels like one coherent course:

1. **Welcome & pitch** — what the skill is in one sentence, and why it's worth 60–90 minutes today.
2. **Prerequisites** — explicitly minimal; free tools only; OS/install requirements noted where they exist.
3. **Session roadmap** — a minute-by-minute agenda for one sitting.
4. **Core concepts** — the 3–5 ideas a beginner must understand, explained with analogies.
5. **Hands-on exercise** — numbered "do it now" steps with an expected result, so the learner ends the session having *done* something real.
6. **Cheat sheet** — key terms / commands / shortcuts for quick reference.
7. **Common beginner mistakes** — day-one pitfalls and how to dodge them.
8. **Check yourself** — a 5-question self-quiz with answers at the bottom.
9. **Homework & what's next** — one small practice task for the week plus a preview of Lesson 2.

**Ground rules:** every lesson stands alone (no "read the docs first", no paid accounts), jargon is defined the moment it appears, analogies before formalism, and nothing existing in the repo is modified or deleted — only new files are added.

---

## 4. Lesson inventory & session content

| # | Folder | First session covers |
|---|---|---|
| 1 | **Terminal** | What the shell is; `pwd`, `ls`, `cd`, `mkdir`; navigating without the file explorer |
| 2 | **Keyboard** | Touch typing: posture, home row, baseline WPM test, first drill routine |
| 3 | **Python** | Installing Python, the REPL, variables, first script run from the terminal |
| 4 | **JavaScript** | Browser console, variables, functions, first interactive script |
| 5 | **APIs** | What an API is, JSON, first real GET request against a free public API |
| 6 | **Web Design** | Layout, typography, color; sketching and evaluating a first wireframe |
| 7 | **WSL** | What WSL is for, installing Ubuntu, first commands, Windows ↔ WSL file interop |
| 8 | **CI-CD** | What a pipeline is; a first GitHub Actions workflow that runs on push |
| 9 | **n8n** | Workflow automation concept; building a first two-node workflow end to end |
| 10 | **Notion** | Blocks, pages, databases; building a first personal dashboard |
| 11 | **vector databases** | What embeddings are (intuition first); first search via a free playground/no-code demo |
| 12 | **Content Creation** | Finding an idea, simple structure, writing and shipping one first piece of content |
| 13 | **SEO** | How search engines work, keywords, optimizing a first page title and description |
| 14 | **product creator** | Choosing a first digital-product idea and outlining a minimal version |
| 15 | **product-marketing skills** | Audience, positioning; writing a first one-line pitch and landing headline |
| 16 | **service-communication skills** | Tone, empathy, structure; rewriting a first customer reply |

---

## 5. Execution order

Grouped so related skills stay consistent in tone and cross-references:

1. **Foundations:** Terminal → Keyboard → Python → JavaScript
2. **Web & DevOps:** APIs → Web Design → WSL → CI-CD
3. **Automation & Knowledge:** n8n → Notion → vector databases
4. **Business & Content:** Content Creation → SEO → product creator → product-marketing skills → service-communication skills

Where skills connect (e.g. Python ↔ Terminal, APIs ↔ JavaScript), lessons cross-link to each other's `First Lesson.md` so the collection doubles as a natural learning path.

---

## 6. Progress checklist

Total: **17 new files** (1 × `Plan.md` + 16 × `First Lesson.md`). Nothing existing is modified.

- [x] `Plan.md` (this file)
- [x] `Terminal/First Lesson.md`
- [x] `Keyboard/First Lesson.md`
- [x] `Python/First Lesson.md`
- [x] `JavaScript/First Lesson.md`
- [x] `APIs/First Lesson.md`
- [x] `Web Design/First Lesson.md`
- [x] `WSL/First Lesson.md`
- [x] `CI-CD/First Lesson.md`
- [x] `n8n/First Lesson.md`
- [x] `Notion/First Lesson.md`
- [x] `vector databases/First Lesson.md`
- [x] `Content Creation/First Lesson.md`
- [x] `SEO/First Lesson.md`
- [x] `product creator/First Lesson.md`
- [x] `product-marketing skills/First Lesson.md`
- [x] `service-communication skills/First Lesson.md`

---

## 7. Assessment — Test1

Added as **Phase 2** of the mission: one graded test per lesson, taken after completing the First Lesson and its homework. Same filename (`Test1.md`) and identical structure in all 16 folders, so progress is comparable across skills.

**Format (50 points, 35-minute cap):**

| Part | What | Points |
|---|---|---|
| A — Concept check | 4 short-answer questions on core ideas | 8 |
| B — Fill the gaps | 4 completion items (exact command/term/value) | 8 |
| C — Hands-on practical | 1 real task, rubric-scored (12 works / 5 explained / 3 extended) | 20 |
| D — Diagnose the mistake | 2 broken scenarios: spot the bug + state the fix | 8 |
| E — Apply & extend | 1 transfer question to a new situation | 6 |

- **Closed book** for Parts A, B, D, E; Part C may use the lesson's cheat sheet only.
- **Scoring bands:** 45–50 excellent · 35–44 solid pass (review misses) · 25–34 re-read flagged lesson sections · <25 redo the First Lesson hands-on.
- **Answer key with model answers** at the bottom of every test.
- **Content rule:** every question references what that lesson actually taught (the six API calls, the Books database, the AER rewrite, the baseline WPM, the red-X pipeline, ...); Part C and E always use a *new* situation to test transfer, not memory.

### Test1 checklist

- [x] `Terminal/Test1.md`
- [x] `Keyboard/Test1.md`
- [x] `Python/Test1.md`
- [x] `JavaScript/Test1.md`
- [x] `APIs/Test1.md`
- [x] `Web Design/Test1.md`
- [x] `WSL/Test1.md`
- [x] `CI-CD/Test1.md`
- [x] `n8n/Test1.md`
- [x] `Notion/Test1.md`
- [x] `vector databases/Test1.md`
- [x] `Content Creation/Test1.md`
- [x] `SEO/Test1.md`
- [x] `product creator/Test1.md`
- [x] `product-marketing skills/Test1.md`
- [x] `service-communication skills/Test1.md`

---

## 8. Verification plan

After each phase:

1. Confirm all 16 `First Lesson.md` and 16 `Test1.md` files exist in the correct folders.
2. Spot-check that every lesson contains all 9 template sections and every test contains all 5 parts + answer key.
3. Confirm cross-links point to existing files.
4. Confirm no pre-existing file (e.g. `Notion/Notion export.md`) was modified or deleted.
