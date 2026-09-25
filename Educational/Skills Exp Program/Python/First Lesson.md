# First Lesson — Python

> **Welcome!** Python is the world's most beginner-friendly programming language — you write instructions in near-English and the computer obeys. Today you will install Python, have your first conversation with it, and write and run a real program. One session from now, you will officially be someone who codes.

---

## 1. Why learn this?

- Python powers data analysis, AI, automation, web backends, and scientific research — it's the language people reach for to *do things with computers*.
- It reads like English, so you learn programming concepts without fighting syntax.
- Ten lines of Python can replace an hour of copy-pasting in a spreadsheet.

**Where the other lessons meet this one:** you'll run Python from the [Terminal](../Terminal/First%20Lesson.md) — do that lesson first if the terminal feels scary. Later, Python plus [APIs](../APIs/First%20Lesson.md) is how you fetch data from the internet automatically.

---

## 2. Prerequisites

- A computer (Windows, macOS, or Linux) with internet for the install.
- Basic terminal comfort (typing commands and pressing Enter). If not: do the [Terminal First Lesson](../Terminal/First%20Lesson.md) first — it's 75 minutes.
- Python itself — install it now:
  - **Windows:** go to **python.org/downloads**, run the installer, and **check the box "Add Python to PATH"** (this is the #1 beginner install mistake — don't skip it).
  - **macOS:** `brew install python` (if you have Homebrew), or use the python.org installer.
  - **Linux:** usually pre-installed; otherwise `sudo apt install python3`.

---

## 3. Session roadmap (~90 minutes)

| Time | Activity |
|---|---|
| 0–15 min | Verify the install (`python --version`) |
| 15–35 min | The REPL: your first conversation with Python |
| 35–55 min | Core concepts: variables, types, f-strings |
| 55–80 min | Write and run your first real script |
| 80–90 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 A program is a recipe
Computers follow instructions *exactly*, in order, with zero imagination. Programming is writing a recipe so precise that a very fast, very literal cook can follow it. Bugs happen when the recipe is ambiguous — the computer always does what you *said*, not what you *meant*.

### 4.2 Variables are labeled boxes
```python
name = "Maya"
age = 29
```
`name` is a label on a box containing the text `"Maya"`. Later lines can use `name` instead of retyping the value — and if you change the box's contents, everything using the label sees the new value.

### 4.3 Types matter
Two basic types today:
- **str** (string): text, always in quotes — `"hello"`.
- **int** (integer): whole numbers — `42`.

They behave differently: `"2" + "2"` glues text into `"22"`, while `2 + 2` adds to `4`. Most beginner bugs are type confusion.

### 4.4 Functions are machines with a name
```python
print("Hello!")
```
`print` is a function — a pre-built machine: you hand it input (inside the parentheses), it does its job. You'll also `input()` to *receive* from the user. Later you'll write machines of your own.

### 4.5 The REPL vs. scripts
The **REPL** (Read-Eval-Print Loop) is a live conversation: you type one line, Python answers instantly. A **script** is a saved `.py` file run start-to-finish. REPL is the sketchpad; scripts are the finished drawing. Today you'll use both.

---

## 5. Hands-on exercise

**Part A — Meet the REPL (15 min)**

Open your terminal and type:
```
python
```
(On macOS/Linux try `python3` if `python` isn't found.) You should see the version and a `>>>` prompt — Python is listening. Try each line, one at a time, and *predict before you press Enter*:

```python
>>> 2 + 2
>>> 10 * 3
>>> "hello" + " world"
>>> "2" + "2"
>>> print("I am talking to a computer")
>>> name = "Maya"
>>> print("Hi, " + name)
>>> len("elephant")
>>> exit()
```

Notice: the REPL echoes results automatically; `print` is how scripts display text. Notice `"2" + "2"` — did you predict `"22"`?

**Part B — Your first script (25 min)**

**Step 1.** In the terminal:
```
mkdir python-practice
cd python-practice
```

**Step 2.** Create a file named `hello.py` using any plain-text editor (Notepad, TextEdit in plain-text mode, or VS Code). Type this exactly:

```python
# My first Python program
name = input("What is your name? ")
age = input("How old are you? ")
age_number = int(age)

print("Hello, " + name + "!")
print("Next year you will be", age_number + 1)
print("In ten years you will be", age_number + 10)
```

The `#` line is a **comment** — a note for humans; Python ignores it.

**Step 3.** Save the file, then in the terminal (inside `python-practice`):
```
python hello.py
```

**Step 4.** Answer the prompts. Expected output:
```
What is your name? Maya
How old are you? 29
Hello, Maya!
Next year you will be 30
In ten years you will be 39
```

**Step 5 — Make it yours (the real lesson).** Change the program: add a question ("What city do you live in?") and another printed line using the answer. Run it again. Breaking and fixing your own edits is how programming actually feels — this loop *is* the skill.

**Expected result:** a file `hello.py` that asks questions and prints a personal reply, which you created and modified yourself.

---

## 6. Cheat sheet

| Thing | Example | Meaning |
|---|---|---|
| Start REPL | `python` (or `python3`) | live one-line-at-a-time mode |
| Leave REPL | `exit()` | back to the terminal |
| Run a script | `python hello.py` | executes the whole file |
| Variable | `name = "Maya"` | label a value |
| String | `"text"` | text, needs quotes |
| Integer | `42` | whole number |
| Print | `print("hi")` | show output |
| Read input | `input("prompt")` | ask the user (always returns a string!) |
| Convert | `int("29")` | string → number |
| Comment | `# note` | ignored by Python |
| f-string | `f"Hi {name}"` | neat way to put variables in text |

---

## 7. Common beginner mistakes

1. **"Add Python to PATH" unchecked (Windows).** If the terminal says `'python' is not recognized`, re-run the installer and check that box.
2. **Quotation mismatch.** Strings need matching quotes: `"hello'` is an error.
3. **`input()` always gives you a string.** `"5" + 5` crashes. Convert with `int()` when you need math.
4. **Case sensitivity.** `Print` ≠ `print`. Python is precise.
5. **Editing a file but running an old copy.** Always save before `python hello.py` — and make sure you're in the right folder.

---

## 8. Check yourself

1. What's the difference between the REPL and a `.py` script?
2. What does `input()` return, and why did our script need `int()`?
3. What will `print("3" + "4")` display — and what would `print(3 + 4)` display?
4. What does a line starting with `#` do?
5. Your terminal says `python: command not found`. Name two things to check.

<details><summary><strong>Answers</strong></summary>

1. REPL: interactive, one line at a time, great for experiments. Script: a saved file run top-to-bottom, great for real programs.
2. A string (text). Because you can't do math on text, so we converted with `int()`.
3. `"3" + "4"` glues text → `34`; `3 + 4` adds numbers → `7`.
4. It's a comment — a human-readable note that Python ignores.
5. (a) Python may not be installed or wasn't added to PATH — re-run the installer; (b) on macOS/Linux, try `python3` instead.
</details>

---

## 9. Homework & what's next

**This week's homework:** write a `madlibs.py` that asks for a name, a place, a number, and an animal, then prints a short silly story using all four answers. Bonus: make the number affect the story (e.g., "I saw **12** capybaras").

**Lesson 2 preview:** `if` decisions, `for` loops, and lists — the moment your programs start making choices and doing repetitive work for you.

**Where to go next in this collection:** [APIs](../APIs/First%20Lesson.md) (fetch real data from the internet), [Terminal](../Terminal/First%20Lesson.md) (the room Python runs in), and someday [vector databases](../vector%20databases/First%20Lesson.md) — which are best explored *through* Python.
