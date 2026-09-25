# First Lesson — CI/CD

> **Welcome!** CI/CD (Continuous Integration / Continuous Delivery) is the practice of having robots check and ship your code every time you save it. Instead of "works on my machine" surprises, a **pipeline** runs your tests and deploys automatically. Today you will build a real pipeline on GitHub — free, no credit card — and watch it run.

---

## 1. Why learn this?

- Every professional software team uses CI/CD; "I know GitHub Actions" is a real resume line.
- It removes the most boring, error-prone part of software work (manual testing + deploying) and hands it to a machine.
- It changes how you feel about your code: every push is verified by an impartial robot.

**Where the other lessons meet this one:** pipelines run on Linux, so anything from the [WSL First Lesson](../WSL/First%20Lesson.md) transfers directly. [Terminal](../Terminal/First%20Lesson.md) and [Python](../Python/First%20Lesson.md) skills let you write the commands the pipeline executes.

---

## 2. Prerequisites

- A **GitHub account** (free — github.com).
- Basic terminal comfort (see [Terminal First Lesson](../Terminal/First%20Lesson.md)) and the ability to type a URL.
- No installs needed today: GitHub's servers run the pipeline for you.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | What CI and CD actually stand for |
| 10–25 min | GitHub + a repo + the Actions tab tour |
| 25–50 min | Build your first workflow: commit → watch it run |
| 50–65 min | Break it on purpose, read the logs |
| 65–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 CI: Continuous Integration
Every time you push code, a machine: checks out your code, installs dependencies, runs your tests/linters/build. If something broke, you know *which push* broke it — immediately, not three weeks later. Integration pain goes from "dreaded merge day" to "green checkmark."

### 4.2 CD: Continuous Delivery (or Deployment)
After tests pass, the pipeline can automatically package or ship the app — to a staging server, an app store, an npm package. "Delivery" means it's *ready* to release on one click; "deployment" means it releases itself.

### 4.3 The pipeline is a recipe of jobs
A pipeline is a file in your repo describing **jobs** made of **steps**:

```yaml
name: My First Pipeline
on: push
jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Say hello
        run: echo "Hello from the robot!"
```

Read it like English: *when code is pushed, on an Ubuntu machine, run these steps in order.* That file format is **YAML** — indentation matters (2 spaces, never tabs).

### 4.4 Triggers, runners, and the green check
- **Trigger:** the event that starts the pipeline (`on: push`, `on: pull_request`, timers, manual buttons).
- **Runner:** the fresh virtual machine (Ubuntu, Windows, macOS) that executes your jobs — a clean computer every run, which is why "works in CI" means something.
- **Status check:** the ✅/❌ next to each commit. Green = robot approves.

---

## 5. Hands-on exercise

**Step 1 — Create a repo (5 min).** On github.com: **New repository** → name it `ci-practice` → Public → check **Add a README** → Create.

**Step 2 — Meet the Actions tab (5 min).** Click the **Actions** tab. GitHub suggests starter workflows; ignore them for now. Notice: this tab is where pipeline runs appear. Right now it's empty — that's about to change.

**Step 3 — Create your first workflow (10 min).** In the repo: **Add file → Create new file**. For the name, type the path itself:

```
.github/workflows/hello.yml
```

Typing the `/` in the filename creates the folders automatically. Paste:

```yaml
name: My First Pipeline
on: push
jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Say hello
        run: echo "Hello from the robot!"
      - name: Show the time
        run: date
      - name: List files
        run: ls -la
```

Commit the file (green **Commit changes** button).

**Step 4 — Watch it run (10 min).** Go to **Actions** → click the run that just appeared (named after your commit message) → click the `greet` job. You'll see your steps execute live: the echo, the date, the `ls -la` output showing your README. When it finishes: **green checkmark.** You built a pipeline. Take the moment.

**Step 5 — Make it react to your code (10 min).** Add a tiny Python file `app.py` to the repo (Add file → Create new file):

```python
# app.py
print("2 + 2 =", 2 + 2)
```

Then update `hello.yml` — add these steps at the end of `steps:` (mind the indentation!):

```yaml
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run the app
        run: python app.py
```

`uses:` pulls in a ready-made action someone else wrote (that's the ecosystem's superpower); `run:` executes shell commands. Push/commit, watch the run: the robot now checks out your code, installs Python, and runs your program.

**Step 6 — Break it on purpose (10 min).** Edit `app.py` to say `print("2 + 2 =", 2 + "2")` and commit. Watch Actions: **red X.** Click into the failing job and find the error in the log. This is the entire value of CI: the robot caught the bug *before a human ever ran the code*. Fix it, commit, watch it go green again.

**Expected result:** a repo with a working pipeline that runs on every push, including one deliberate red-X experience — which is exactly what CI feels like in real life.

---

## 6. Cheat sheet

| Term | Meaning |
|---|---|
| CI | automatic checks on every push |
| CD | automatic delivery/deployment after checks pass |
| Pipeline / workflow | the recipe file (`.github/workflows/*.yml`) |
| Trigger (`on:`) | what starts a run: push, PR, schedule |
| Job | a group of steps on one runner |
| Runner | the fresh VM that executes jobs |
| `run:` | shell command step |
| `uses:` | reuse someone else's packaged steps |
| YAML | config format; 2-space indentation, no tabs |
| Green ✅ | all jobs passed |
| Red ❌ | something failed — read the log, the line number is in there |

---

## 7. Common beginner mistakes

1. **Tabs in YAML.** YAML forbids them. Two spaces, always. This single rule causes most first-day failures.
2. **Wrong file path.** It must be exactly `.github/workflows/anything.yml` — otherwise GitHub ignores it.
3. **`uses:` and `run:` mixed in one step.** A step does one or the other.
4. **Expecting deployments on day one.** Today's pipeline only *checks*. Deploying to real servers involves secrets and credentials — Lesson 2+.
5. **Treating red X as failure of *you*.** A failing pipeline is the system *working*. Read the log bottom-up; the error message names the step.

---

## 8. Check yourself

1. What do CI and CD each stand for, in plain words?
2. Where must a workflow file live in the repo, and what format is it?
3. What's the difference between `run:` and `uses:`?
4. What event started your pipeline today, and where would you change that?
5. Your commit shows a red ❌. What are the first two things you do?

<details><summary><strong>Answers</strong></summary>

1. CI: every push is automatically built and tested. CD: after checks pass, the app is automatically packaged/shipped.
2. `.github/workflows/<name>.yml`, written in YAML.
3. `run:` executes your shell commands; `uses:` runs a pre-packaged action from the community.
4. `on: push`. Change the `on:` section (e.g., `on: [push, pull_request]`).
5. Open the Actions tab → click the failed run → read the log for the failed step (bottom-up), fix the named problem, push again.
</details>

---

## 9. Homework & what's next

**This week's homework:** add a linter step to your pipeline — set up Python with `actions/setup-python@v5` and add a step `run: python -m json.tool ci-practice.json` on a small JSON file you add, or lint your YAML with `run: pip install yamllint && yamllint .github/workflows/`. Goal: a pipeline with 3+ steps that catches a real mistake.

**Lesson 2 preview:** testing for real (pytest runs in CI), caching, secrets (how pipelines log into things safely), and deploying a static site to GitHub Pages on green.

**Where to go next in this collection:** [WSL](../WSL/First%20Lesson.md) (runners are Linux; practice the environment locally), [Python](../Python/First%20Lesson.md) (write the code being tested), and [n8n](../n8n/First%20Lesson.md) (a different kind of automation — visual, not code).
