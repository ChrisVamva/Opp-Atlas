# First Lesson — WSL (Windows Subsystem for Linux)

> **Welcome!** WSL lets you run a real Linux environment *inside* Windows — no dual-boot, no virtual machine juggling, no second computer. One command installs it. Today you'll turn your Windows machine into a Linux one, learn why that's valuable, and move files between the two worlds.

---

## 1. Why learn this?

- The professional software world speaks **Linux**: servers, containers, cloud platforms, most tutorials, and tools like Docker all assume it. Windows alone leaves you locked out of much of it.
- WSL gives you Linux *and* Windows together — edit in Windows apps, run in Linux, instantly.
- It's the on-ramp to dev-ops skills: [CI-CD](../CI-CD/First%20Lesson.md) pipelines and servers behave like Linux.

**Where the other lessons meet this one:** WSL is the best terminal on Windows — pair it with the [Terminal First Lesson](../Terminal/First%20Lesson.md) for command skills, and run your [Python](../Python/First%20Lesson.md) scripts inside it exactly as professionals do.

---

## 2. Prerequisites

- **Windows 10 (version 2004+) or Windows 11.** Not available on macOS/Linux (they already have real terminals).
- Administrator rights on the PC for the one-time install.
- ~30 minutes and an internet connection.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | What WSL is (and isn't) |
| 10–30 min | Install WSL + Ubuntu |
| 30–45 min | First Linux commands; create your Linux user |
| 45–60 min | File interop: Windows ↔ WSL |
| 60–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 One command line, two worlds
WSL runs a genuine Linux system alongside Windows. Apps inside it use Linux commands and Linux software; Windows apps keep running normally. It's not an emulator pretending — it's real Linux, made neighbourly.

### 4.2 Distributions: WSL installs a "distro"
A **distribution** (distro) is a flavor of Linux — Ubuntu is the friendly, most documented one, and the default. "Installing WSL" really means "installing Ubuntu inside WSL."

### 4.3 The file systems are neighbors
Each world sees the other's files:
- From WSL, Windows drives appear under `/mnt/` — your C: drive is `/mnt/c/...`.
- From Windows, WSL's Linux files live at `\\wsl$\Ubuntu\home\yourname` (type that into File Explorer).
You can open a file with Windows apps and run it with Linux tools. This interop is WSL's killer feature.

### 4.4 Linux has a package manager
`apt` (Advanced Package Tool) installs software from trusted repositories with one command — no downloading installers from websites, no "Next, Next, Finish":

```
sudo apt update
sudo apt install htop
```

`sudo` means "do this as administrator" (superuser do). Linux folks consider this one of the OS's best ideas.

### 4.5 The terminal is the main interface
Linux culture is terminal-first: most tools assume you type commands. That's why WSL + [Terminal](../Terminal/First%20Lesson.md) skills multiply each other.

---

## 5. Hands-on exercise

**Step 1 — Install (10 min).** Open **PowerShell as Administrator** (`Start` → type `powershell` → right-click → Run as administrator) and run:

```
wsl --install
```

This enables WSL and installs Ubuntu. **Restart the PC when it finishes.** On first launch, Ubuntu asks for a username and password — this is a *Linux* user, separate from your Windows login. Pick something simple; the password matters for `sudo`.

**Step 2 — Confirm you're in Linux (5 min).** Open Ubuntu from the Start menu (or any terminal, then type `wsl`). Run:

```
uname -a
cat /etc/os-release
```

You should see "Ubuntu" in the output. Welcome to Linux.

**Step 3 — First Linux commands (10 min).** Try:

```
pwd
ls
ls -la
cd ~
mkdir wsl-practice
cd wsl-practice
echo "Made in WSL" > note.txt
cat note.txt
```

Notice `ls -la` shows *hidden* files (dot-files) and permissions — Linux shows you more. These are the same commands from the [Terminal First Lesson](../Terminal/First%20Lesson.md); they work identically here.

**Step 4 — Meet apt (10 min).**

```
sudo apt update
sudo apt install tree
tree
```

`tree` draws your folder structure as a diagram. You installed Linux software in three commands — no browser, no installer wizard.

**Step 5 — Cross the border (15 min).**

*Linux → Windows:* create a file on your Windows desktop from inside WSL:
```
echo "Hello from Linux" > /mnt/c/Users/YOUR_WINDOWS_NAME/Desktop/from-wsl.txt
```
Check your actual Windows desktop. It's there.

*Windows → Linux:* in File Explorer's address bar type `\\wsl$\Ubuntu\home\` and press Enter — you're browsing the Linux file system. Or from PowerShell: `wsl cat ~/wsl-practice/note.txt`.

**Step 6 — One Windows command to know:** `wsl --list --verbose` shows which distros are installed and running.

**Expected result:** WSL + Ubuntu installed, a `wsl-practice` folder in your Linux home, a file you created on your Windows desktop *from Linux*, and the ability to browse Linux files from Windows.

---

## 6. Cheat sheet

| Command | Meaning |
|---|---|
| `wsl --install` | install WSL + Ubuntu (Admin PowerShell, one-time) |
| `wsl` | enter Linux from any terminal |
| `wsl --list --verbose` | list installed distros and state |
| `sudo <cmd>` | run command as administrator (asks your Linux password) |
| `apt update` | refresh the software catalog |
| `apt install <pkg>` | install software |
| `/mnt/c/...` | Windows C: drive, as seen from Linux |
| `\\wsl$\Ubuntu\home\...` | Linux home, as seen from Windows Explorer |
| `~` | your Linux home folder (`/home/you`) |
| `ls -la` | list including hidden dot-files |
| `exit` | leave the Linux session |

---

## 7. Common beginner mistakes

1. **Putting project files in `/mnt/c` and working on them from WSL.** Cross-boundary file access is *slow*. Keep Linux projects in your Linux home (`~/`); it's dramatically faster. Visit `/mnt/c` only to reach Windows files.
2. **Forgetting which world you're in.** Prompt gives it away: Linux shows `you@machine:~$`; PowerShell shows `PS C:\...`. When a tutorial says "run this," check which side it's for.
3. **Losing the sudo password.** You set it during install; it's separate from Windows. Store it in your password manager.
4. **Skipping `sudo apt update` first.** The catalog must be refreshed or installs can fail confusingly.
5. **Assuming WSL is a sandbox to break.** It's more durable than that — but `sudo rm` commands still delete things permanently. Same caution as any terminal.

---

## 8. Check yourself

1. What does WSL let you do that a virtual machine also does — but with less overhead?
2. From inside WSL, where do you find your Windows Desktop?
3. What does `sudo` do, and whose password does it ask for?
4. Why keep Linux project files in `~/` rather than `/mnt/c`?
5. What single PowerShell command installs WSL with Ubuntu?

<details><summary><strong>Answers</strong></summary>

1. Run a real Linux environment on Windows; WSL does it lightweight, integrated, and near-native speed.
2. `/mnt/c/Users/YOUR_NAME/Desktop`
3. Runs the command with administrator privileges; it asks for your **Linux** user password (set during install).
4. The 9P file bridge across `/mnt` is much slower than Linux's native file system — noticeable on real projects.
5. `wsl --install` (in an administrator PowerShell).
</details>

---

## 9. Homework & what's next

**This week's homework:** inside WSL, install `htop` (`sudo apt install htop`) and run it — a live view of your machine. Then create `~/notes/` with three `.txt` files and view them from Windows Explorer via `\\wsl$`. Finally run your [Python](../Python/First%20Lesson.md) `hello.py` inside WSL if you've done that lesson.

**Lesson 2 preview:** shells and dotfiles (`bashrc`), SSH keys, `git` setup inside WSL, and VS Code's WSL integration — editing in Windows while running in Linux.

**Where to go next in this collection:** [Terminal](../Terminal/First%20Lesson.md) (deepen command skills), [CI-CD](../CI-CD/First%20Lesson.md) (pipelines run on Linux servers — your WSL skills transfer directly), and [Python](../Python/First%20Lesson.md).
