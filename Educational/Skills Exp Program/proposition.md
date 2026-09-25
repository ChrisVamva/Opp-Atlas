# Proposition — Taking the Skills Vault to the Next Level

> **Scope:** `Documents/Obsidian Vaults/Code/Skills` — an Obsidian vault of 16 skill folders, each containing `First Lesson.md` + `Test1.md` (32 skill files; 34 markdown files in total, including root `Plan.md` and `Notion/Notion export.md`).
> **Decisions confirmed with the owner:** folders stay **flat** (grouping via index notes, not physical moves) · **full Obsidian** features are allowed (frontmatter, Dataview, templates, tags).

---

## 1. Where we are (audit)

**What works well**
- One consistent 9-part lesson template and one consistent 5-part test format across all 16 skills.
- Cross-links between lessons already form a learning path (e.g. Python ↔ Terminal ↔ APIs).
- Answer keys are self-graded with `<details>` blocks — good for review.

**What holds it back**
1. **No entry point.** No README/index — you land in 16 folders with no map, no recommended order, no way to see what's done.
2. **Zero metadata.** No frontmatter, no tags, no status, no scores recorded anywhere. "Progress" exists only in your head.
3. **Dead-end promises.** Every First Lesson teases a "Lesson 2" and homework that nothing follows up on.
4. **Naming drift.** `product creator`, `service-communication skills`, `vector databases` (lowercase + spaces) vs `CI-CD`, `Web Design` — inconsistent casing/spacing.
5. **No way to grow.** Adding skill #17 means inventing structure from scratch; there are no templates for the vault itself.
6. **No hygiene checks.** Nothing verifies files exist, sections are complete, or links resolve.

---

## 2. Target state (the "next level")

A vault that **routes you, remembers for you, and grows safely**:

```
Skills/
├── README.md                  ← home note: what this vault is, track map, start here
├── Dashboard.md               ← Dataview: progress table + scores, auto-generated
├── Plan.md                    ← (existing mission doc, stays)
├── _Templates/
│   ├── Lesson Template.md     ← the 9-part structure, pre-formatted
│   ├── Test Template.md       ← the 5-part + answer-key structure
│   └── New Skill Scaffold.md  ← checklist for adding a skill folder
├── _Inbox.md                  ← parking lot for new skill ideas
├── APIs/                      ← all 16 skill folders unchanged in place
│   ├── First Lesson.md        ← + YAML frontmatter
│   └── Test1.md               ← + YAML frontmatter (incl. score field)
│   └── ...
└── ... (15 more)
```

**Four capabilities added (in execution order):**

| Priority | Capability | Mechanism |
|---|---|---|
| **1** | **Routing** | `README.md` with the 4 tracks (Foundations · Web & DevOps · Automation & Knowledge · Business & Content), recommended order, and links into every folder |
| **2** | **Content growth** | Close dead-end Lesson 2 promises + write first 2 real Lesson 2s (Terminal, Python) using `_Templates/` |
| **3** | **Memory** | YAML frontmatter on all 32 skill files (deferred ~2 weeks after real usage) |
| **4** | **Dashboard** | Dataview `Dashboard.md` showing real status/score tables (conditional on having scores) |
| **5** | **Growth** | `_Templates/` (Lesson, Test, New Skill Scaffold) |
| **Cut** | **Hygiene** | No folder renames, no check-vault script, no separate `CONVENTIONS.md` |

> **Execution sequence:** Routing → Content growth → Memory → Dashboard → Growth (templated). Cleanup items (renames, validation script) are **out of scope** this pass.

---

## 3. Metadata schema (applied to all 32 skill files — deferred)

[Added ~2 weeks after real usage shows what fields matter]

**Guidance for when you come back to this:**

```yaml
---
skill: Python                 # folder name, human-readable
track: foundations            # foundations | web-devops | automation | business
type: lesson                  # lesson | test
level: 1                      # First Lesson = 1, Lesson 2 = 2, ...
duration_min: 90              # for lessons; time cap for tests
status: not-started           # not-started | in-progress | done  (lessons)
score:                        # tests only: leave empty → 0–50 after grading
tags: [skill/python, track/foundations]
prerequisites: [terminal]     # folder slugs of prerequisite First Lessons
updated: 2026-09-24
---
```

`type` + `score` + `status` are the fields Dataview queries on. `tags` make the graph and search useful immediately even before Dataview.

---

## 4. The dashboard (conditional on having scores)

`Dashboard.md` with 4 Dataview queries (shown only when you have real scores to render):

1. **Lessons table** — skill · level · status · duration, sorted by track; checkbox-style status you edit in frontmatter.
2. **Test scores table** — skill · score / 50 · band (excellent / solid / re-read / redo) computed from the score.
3. **Up next** — lessons with `status: not-started` in your current track.
4. **Needs attention** — scores below 35, and links to the flagged lesson sections.

Net effect: open the vault → one click tells you where you are, what you scored, and what to study next.

---

## 5. Execution plan (new priority order)

### Step 1 — Routing *(highest leverage, do immediately)*

- Create `Skills/README.md`:
  - Vault purpose
  - 4-track map with recommended order (Foundations → Web & DevOps → Automation → Business)
  - Links into all 16 folders
  - File conventions (absorbs any `CONVENTIONS.md`)
- **Why first:** ~30 minutes, zero risk, makes all 32 existing files discoverable
- **Done when:** a newcomer reaches any skill in ≤ 2 clicks

### Step 2 — Close the content gap

- Audit Lesson 2 previews across all 16 lessons; build a **Lesson 2 backlog table** (README section)
- Decide per skill: write a real Lesson 2, or relabel the promise as "what's next" without implying a file exists
- **Why second:** fulfills the core learning loop; these are the "promises" every lesson makes
- **Done when:** no lesson implies a non-existent Lesson 2, and a prioritised backlog exists

### Step 3 — Deliver first two real Lesson 2s

- Choose **Terminal** and **Python** (Foundations-first)
- Create `Terminal/Lesson 2.md` + `Test2.md` and `Python/Lesson 2.md` + `Test2.md` using `_Templates/`
- **Why third:** proves the cycle works on content other than scaffolding
- **Done when:** two Lesson 2 + Test2 pairs exist and the cadence feels sustainable

### Step 4 — Memory (frontmatter)

- Add YAML schema to all 32 skill files (16 `First Lesson.md` + 16 `Test1.md`)
- **Deferred on purpose:** two weeks of real vault use reveals what fields you actually wish you'd tracked
- **Resolve before this step:** slug convention for `prerequisites`, where to put conventions (README vs separate file)
- **Done when:** all 32 files carry valid frontmatter matching the agreed schema

### Step 5 — Dashboard (conditional)

- Create `Dashboard.md` with the 4 queries, but only if you have a few scores to render
- **Gated:** no scores = empty table that reads as broken
- **Done when:** dashboard renders real rows

---

## 6. Risks & guardrails

| Risk | Guardrail |
|---|---|
| Frontmatter edits corrupt a lesson body | Edit only *prepend* blocks; verify file lengths change by exactly the frontmatter lines |
| Dashboard looks broken (empty) | Only build after you have real scores; leave placeholder if not ready |
| Scope creep into renaming folders | Renames **out of scope** this pass; revisit in ~a year if it actually annoys you |
| Lesson 2 false promises | Step 2 explicitly closes them; no more "teasers without content" |
| No usage data guides frontmatter | Deferred ~2 weeks, then fields can be added incrementally |

---

## 7. Definition of done (current pass)

- [ ] `README.md` exists: 4 tracks, recommended order, links to all 16 skills, conventions absorbed
- [ ] No lesson implies a non-existent Lesson 2; a prioritised Lesson 2 backlog exists
- [ ] `Terminal/Lesson 2.md` + `Test2.md` and `Python/Lesson 2.md` + `Test2.md` written
- [ ] Slug convention + CONVENTIONS decision locked in
- [ ] *(Optional)* Frontmatter on all 32 files (if you want immediate tracking)
- [ ] *(Conditional)* Dashboard with real scores if available
- [ ] No folder renames and no validation script — out of scope this pass

---

## 8. Open decisions (from the reprioritised plan)

1. **Backlog location** — README section, or a separate `_Inbox.md`?
2. **Lesson 2 naming** — `Lesson 2.md` / `Second Lesson.md` (mirrors `First Lesson.md`)?
3. **Test2 convention** — `Test2.md` (mirrors `Test1.md`), or a scoreable upgrade?
4. **Timing** — confirm the ~2-week soak before frontmatter, or start sooner?
