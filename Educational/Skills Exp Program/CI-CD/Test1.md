# Test1 — CI/CD

> **When:** after the [First Lesson](First%20Lesson.md) and its linting-step homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What do CI and CD each stand for, in plain words?

**A2.** What is a **runner**, and why does "works in CI" mean something?

**A3.** What's the difference between `run:` and `uses:`?

**A4.** Why is a red ❌ the system *working*, not failing?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Workflow files live in `_____` in the repo (full folder path).

**B2.** The trigger section: `_____: push`

**B3.** YAML indentation uses 2 _____, never tabs.

**B4.** A group of steps on one runner is a `_____`.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Your `ci-practice` repo from the lesson (or a new one).*

Build a pipeline that, **on every push**:

1. Checks out the code (`actions/checkout@v4`).
2. Sets up Python 3.12 (`actions/setup-python@v5`).
3. Runs `python app.py` — where `app.py` prints two things: a greeting and the result of `10 * 3`.
4. Lists the repo's files (`ls -la`).

Then, when it runs **green**: deliberately break `app.py` (e.g., `10 + "3"`), push, and record what the Actions tab showed. Fix it and confirm green again.

**Extension (3 pts):** add a second job that also runs on push, and explain in one comment line what YAML element would let both jobs share work later (artifacts) — name-drop only, no implementation needed.

### Rubric
| Points | Standard |
|---|---|
| 12 | Green run with all four steps; the break/fix cycle completed and recorded |
| 5 | You can explain the workflow file's anatomy (on/jobs/runs-on/steps) |
| 3 | Extension: second job + artifacts named |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A workflow saved at `workflows/hello.yml` (repo root) never appears in the Actions tab.

**D2.** A learner pastes a workflow copied from a blog that indents with **tabs** — the file shows a parse error immediately.

**D3.** *(Bonus scenario, not scored separately)*: one step contains both `uses: actions/checkout@v4` and `run: ls -la`. Why does this fail?

---

## Part E — Apply & extend (6 pts)

Your pipeline is green but a teammate still breaks the app. In **4–6 sentences**, explain what else CI gives a team beyond running tests — using the lesson's terms: *fresh runner*, *status check*, *which push broke it*, and what "integration pain becomes a green checkmark" means.

---

## Score yourself

| Part | Max | Yours |
|---|---|---|
| A | 8 | |
| B | 8 | |
| C | 20 | |
| D | 8 | |
| E | 6 | |
| **Total** | **50** | |

---

## Answer key

<details><summary><strong>Part A</strong></summary>

**A1.** CI: every push is automatically built and tested. CD: after checks pass, the app is automatically packaged/shipped (delivery = ready to release; deployment = releases itself). · **A2.** The fresh virtual machine executing jobs; it starts clean every run, so "works in CI" is reproducible — not "works on my machine." · **A3.** `run:` executes shell commands; `uses:` runs a pre-packaged action from the ecosystem. · **A4.** It caught a bug automatically *before a human ran the code* — exactly the value CI exists to provide.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `.github/workflows/` · **B2.** `on` · **B3.** spaces · **B4.** job
</details>

<details><summary><strong>Part C — model workflow</strong></summary>

```yaml
name: Test1 Pipeline
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run the app
        run: python app.py
      - name: List files
        run: ls -la
```

The break/fix cycle is the graded heart: record the red ❌, read the log for the failing step, fix, re-green. Extension: a second `jobs:` entry (e.g., `lint:`); sharing = upload/download **artifacts** (`actions/upload-artifact`) — naming it is enough at this stage.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: path must be exactly `.github/workflows/<name>.yml` (with the `.github` folder) — GitHub ignores anything else. Fix: move it. · **D2.** Bug: YAML forbids tabs; 2-space indentation only. Fix: convert to spaces. · **D3.** (bonus) A step does one *or* the other: `uses:` runs a packaged action, `run:` executes shell — combining them in one step is invalid.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

Fresh runners make results reproducible (kills "works on my machine"); the red/green status check next to each commit tells the whole team at a glance which push broke the build — the robot caught it, so nobody merged it; integration stops being a dreaded merge-day event and becomes a green checkmark per push. Extra: CI is an impartial reviewer that never gets tired.
</details>
