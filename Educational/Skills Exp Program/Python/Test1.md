# Test1 — Python

> **When:** after the [First Lesson](First%20Lesson.md) and its madlibs homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What is the difference between the REPL and a `.py` script, and when is each the right tool?

**A2.** What does `input()` always return, and what does that force you to remember?

**A3.** What is a comment, and how is one written in Python?

**A4.** What does it mean that Python is "case-sensitive"? Give one example.

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Convert the string `"29"` to the number 29: `_____`

**B2.** Start an interactive session: `_____` (terminal command)

**B3.** The neat way to put a variable inside text: `f"Hi _____"` for a variable `name`.

**B4.** Run the file `hello.py`: `_____ hello.py`

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Work in a file, run from the terminal.*

Write `guest_list.py` that:

1. Asks for the user's **name**, **city**, and **number of guests** (three `input()` prompts).
2. Computes how many tables of 6 are needed for the guests (this requires converting the guest count).
3. Prints a greeting with the name, a line stating the city, and a line stating tables needed.

Expected run:
```
What is your name? Maya
What city? Lisbon
How many guests? 29
Hello, Maya!
City: Lisbon
29 guests need 5 tables of 6.
```

**Extension (3 pts):** handle the case where the user types `0` guests (say so), and explain in one comment *why* the conversion in step 2 is needed.

### Rubric
| Points | Standard |
|---|---|
| 12 | Runs correctly on sample input; all three prompts and outputs work |
| 5 | You can explain each line's job (esp. `int()` conversion) |
| 3 | Extension working + comment present |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner's script has `age = input("Age? ")` then `print("Next year:", age + 1)` — and crashes with `TypeError: can only concatenate str...`.

**D2.** A learner saved `hello.py` but the terminal says `python: command not found` on Windows.

---

## Part E — Apply & extend (6 pts)

You want a script that reads how many minutes you practiced typing this week and tells you whether you hit the 75-minute target (5 days × 15 min). In **4–6 sentences** (no code needed), describe: what `input()` gives you, what you must convert, what the decision is, and which lesson's homework this would extend.

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

**A1.** REPL: interactive, one line at a time, ideal for experiments and checking behavior. Script: saved `.py` run top-to-bottom, ideal for real/ repeatable programs. · **A2.** A **string** — so math requires conversion with `int()`. · **A3.** A human-readable note Python ignores; starts with `#`. · **A4.** Capitalization matters: `Print` ≠ `print`, `Name` ≠ `name` — precise spelling decides whether code runs.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `int("29")` · **B2.** `python` (or `python3`) · **B3.** `{name}` · **B4.** `python`
</details>

<details><summary><strong>Part C — model solution</strong></summary>

```python
# Guest list calculator
name = input("What is your name? ")
city = input("What city? ")
guests = int(input("How many guests? "))

tables = (guests + 5) // 6   # ceiling division: round up

print("Hello, " + name + "!")
print("City: " + city)
print(guests, "guests need", tables, "tables of 6.")
```

Model extension: `if guests == 0: print("No guests — no tables needed.")` — and the comment explains `int()` is needed because `input()` returns a string, and strings can't be used in math.

*(Note for graders: `(guests + 5) // 6` is ceiling division — if a learner uses `math.ceil(guests / 6)`, that's equally correct; the key insight is rounding **up**.)*
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: `input()` returned the string `"29"`, and `"29" + 1` mixes types. Fix: `age = int(input("Age? "))` before the math. · **D2.** Bug: Python either isn't installed or the installer's **"Add Python to PATH"** box was left unchecked. Fix: re-run the installer with PATH checked (verify with `python --version`).
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

`input()` gives a *string*, so minutes must go through `int()` before comparing with 75; the decision is an if/else ("hit target" vs. "X minutes short"); it extends the Keyboard First Lesson's homework log (5 × 15 = 75 min target); recognizing that the comparison is between a number and a number, not text.
</details>
