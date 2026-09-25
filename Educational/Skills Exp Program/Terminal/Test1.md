# Test1 — Terminal

> **When:** after the [First Lesson](First%20Lesson.md) and its homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What is the *working directory*, and which command displays it?

**A2.** In a path, what do `.` and `..` each mean?

**A3.** What does `echo "hi" > file.txt` do differently from `echo "hi"`?

**A4.** Name the two keyboard features the lesson called your best friends, and what each does.

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Create a folder named `photos`: `_____ photos`

**B2.** Jump to your home folder in one command: `cd _____`

**B3.** Print the contents of `note.txt`: `_____ note.txt`

**B4.** On Windows PowerShell, `_____` works as a synonym for `ls`.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Do every step in order, typing each command yourself.*

1. Inside your **home folder**, create a folder named `test1-terminal` and move into it.
2. Inside it, create **two** folders named `notes` and `drafts` — using **one** command.
3. Create a file `todo.txt` containing the line `Finish Terminal Test1`.
4. Display `todo.txt`'s contents on screen.
5. Show a listing proving all three items (two folders + one file) exist.

**Extension (3 pts):** use Tab completion for at least one filename, and `↑` history to re-run any command — then say which you used.

### Rubric
| Points | Standard |
|---|---|
| 12 | All five steps work, in order, no destructive missteps |
| 5 | You can explain, per step, what the command did |
| 3 | Extension completed |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner runs `mkdir my projects` expecting one folder named "my projects" — and gets two folders, `my` and `projects`.

**D2.** On Linux, a learner runs `cd desktop` and gets "No such file or directory" — but `ls` clearly shows a folder named `Desktop`.

---

## Part E — Apply & extend (6 pts)

A friend uses only the file explorer and asks why anyone bothers with the terminal. In **4–6 sentences**, give **two** concrete situations where the terminal wins — correctly using at least **three** commands from today's lesson in your explanation.

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

**A1.** The folder the terminal is currently "standing inside"; every command runs there. Show it with `pwd`. · **A2.** `.` = this folder; `..` = the folder one level up. · **A3.** `echo "hi"` prints to the screen; with `> file.txt` the text is written *into* the file (created if missing) instead. · **A4.** `Tab` completes filenames/commands (prevents typos); `↑` recalls previous commands from history.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `mkdir` · **B2.** `cd ~` · **B3.** `cat` · **B4.** `dir`
</details>

<details><summary><strong>Part C — model solution</strong></summary>

```
cd ~
mkdir test1-terminal
cd test1-terminal
mkdir notes drafts
echo "Finish Terminal Test1" > todo.txt
cat todo.txt
ls
```
Key insight: step 2 is the one-command two-folder trick — `mkdir notes drafts` creates both at once (the "space means two names" behavior, used intentionally).
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: unquoted space splits the name into two arguments. Fix: `mkdir "my projects"` (quotes) or `mkdir my-projects` (no space). · **D2.** Bug: case sensitivity — `desktop` ≠ `Desktop` on Linux/macOS. Fix: type the exact case, or use Tab completion to get it right.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

Two real wins (e.g., creating a folder structure for 20 projects in seconds with `mkdir`; reading a file without opening an app via `cat`; jumping anywhere instantly with `cd ~`), with commands used correctly and spelled (pwd, ls, cd, mkdir, echo >, cat). Speed + scripting/muscle-memory arguments welcome; "it looks cool" is not.
</details>
