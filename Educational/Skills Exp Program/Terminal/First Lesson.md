# First Lesson — Terminal

> **Welcome!** The terminal (also called the command line or shell) is a way to control your computer by *typing commands* instead of clicking. Today you will open a real terminal, move through your folders, and create your first files — no mouse required. By the end of this session you will understand why programmers, data analysts, and automation builders all live in this black window.

---

## 1. Why learn this?

- Almost every tutorial for programming, data work, servers, and automation assumes you can use the terminal.
- It is *faster* than clicking once your hands learn it — and it can be scripted, meaning the computer repeats your work for you.
- It is the same on every machine: the skills you learn today work on Windows, macOS, and Linux.

**Where the other lessons meet this one:** [Python](../Python/First%20Lesson.md) and [WSL](../WSL/First%20Lesson.md) both assume you can type commands comfortably. This lesson is the doorway to both.

---

## 2. Prerequisites

- A computer. That's all.
- No installs needed:
  - **Windows:** press `Start`, type `Terminal` or `PowerShell`, press Enter.
  - **macOS:** open **Terminal** from Applications → Utilities (or press `Cmd + Space`, type `terminal`, Enter).
  - **Linux:** usually `Ctrl + Alt + T`.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | Open a terminal, understand the prompt |
| 10–30 min | Learn `pwd`, `ls`, `cd` — moving around |
| 30–45 min | Create things: `mkdir`, file creation |
| 45–60 min | Read and search: `cat`, history, Tab completion |
| 60–75 min | Hands-on exercise + quiz |

---

## 4. Core concepts

### 4.1 The prompt is a question
When you open the terminal you see something like `C:\Users\you>` or `you@laptop:~$`. This is the **prompt**. It means: *"I'm listening — type a command and press Enter."* The path shown is your **current location**.

### 4.2 You are always *somewhere*
The terminal is always "standing inside" one folder, called the **working directory**. Every command you run happens there — like standing in one room of a house and only being able to touch things in that room until you walk somewhere else.

### 4.3 Commands have the shape: verb + arguments
```
command   argument    argument
  cd       Documents
  mkdir    my-project
```
The command is the verb. The arguments tell it *what* to act on. Many commands also accept **options** (extra flags like `-a`) that change their behavior.

### 4.4 The terminal forgives — mostly
Typing a wrong command usually just prints an error. The truly dangerous commands (deleting things) announce themselves, and today we simply won't use them.

---

## 5. Hands-on exercise: build a practice workspace

Do these in order. Type them yourself — don't copy-paste. Muscle memory is the point.

**Step 1 — Find out where you are**
```
pwd
```
*"print working directory."* On Windows PowerShell the equivalent is simply typing `pwd` too (it works there as well).

**Step 2 — Look around**
```
ls
```
*"list."* You should see the files and folders of your current location. (Windows PowerShell also accepts `dir`.)

**Step 3 — Walk into a folder and back**
```
cd Desktop
ls
cd ..
```
`cd` = "change directory." `..` always means "the folder above this one." Repeat until comfortable: go down, come back up.

**Step 4 — Go home instantly**
```
cd ~
```
`~` means your home folder, wherever you are.

**Step 5 — Create a practice area**
```
mkdir terminal-practice
cd terminal-practice
```
`mkdir` = "make directory" (folder). Check with `ls` that it's empty.

**Step 6 — Create a file (no mouse!)**
```
echo "Hello, terminal" > hello.txt
```
`echo` prints text; the `>` sends that text *into* a file instead of the screen. Verify:
```
ls
cat hello.txt
```
`cat` prints a file's contents. You should see your sentence again.

**Expected result:** a folder `terminal-practice` on your home/desktop area containing `hello.txt`, created entirely by typing.

**Step 7 — Two power moves**
- **Tab completion:** type `cat he` then press `Tab` — the terminal finishes the filename for you. Use this forever; it prevents typos.
- **History:** press the **↑ arrow** to recall previous commands.

---

## 6. Cheat sheet

| Command | Meaning | Notes |
|---|---|---|
| `pwd` | print working directory | "Where am I?" |
| `ls` | list files | Windows also: `dir` |
| `cd folder` | change directory | |
| `cd ..` | go up one level | `cd ~` = home |
| `mkdir name` | make a new folder | |
| `echo text > file` | write text to a file | creates it if missing |
| `cat file` | print file contents | |
| `Tab` | auto-complete | best friend |
| `↑` / `↓` | command history | |

---

## 7. Common beginner mistakes

1. **Spaces matter.** `mkdir my folder` makes *two* folders (`my` and `folder`). Use quotes or hyphens: `mkdir "my folder"` or `mkdir my-folder`.
2. **Case sensitivity.** On Linux/macOS, `Desktop` and `desktop` are different. If `cd` fails, check the exact name with `ls`.
3. **Fear of breaking everything.** Today's commands are read-and-create only. Cautious exploration is how everyone learns.
4. **Copy-pasting multi-line blocks blindly.** Type commands one line at a time and watch what each does.

---

## 8. Check yourself

1. What command tells you which folder you are currently in?
2. How do you go up one level? How do you jump to your home folder?
3. What does `mkdir photos` do, and where does the new folder appear?
4. What's the difference between `echo hi` and `echo hi > note.txt`?
5. Which two keys save you the most typing every single day?

<details><summary><strong>Answers</strong></summary>

1. `pwd`
2. `cd ..` goes up; `cd ~` goes home.
3. It creates an empty folder named `photos` inside your current working directory.
4. `echo hi` prints `hi` to the screen; `echo hi > note.txt` writes `hi` into a file named `note.txt`.
5. `Tab` (completion) and `↑` (history).
</details>

---

## 9. Homework & what's next

**This week's homework:** for the next 3 days, do one small task per day only in the terminal — e.g., create a folder of notes, list your Downloads folder, or write one text file. Five minutes a day builds the reflex.

**Lesson 2 preview:** reading files, moving/renaming (`mv`, `cp`), and understanding *paths* — plus why every programmer's terminal looks different (shells and profiles).

**Where to go next in this collection:** [Python](../Python/First%20Lesson.md) runs its first script *from* the terminal; [WSL](../WSL/First%20Lesson.md) gives Windows users a real Linux terminal.
