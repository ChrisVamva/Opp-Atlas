# Test1 — WSL

> **When:** after the [First Lesson](First%20Lesson.md) and its htop/notes homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What does WSL give you that a virtual machine also gives — but with less overhead?

**A2.** From *inside* WSL, where is your Windows C: drive? From *Windows* Explorer, where is your Linux home?

**A3.** What does `sudo` do, and which password does it ask for?

**A4.** What is a Linux distro, and which one does `wsl --install` give you?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Refresh the software catalog before installing: `sudo apt _____`

**B2.** Install the `htop` package: `sudo apt _____ htop`

**B3.** The one-time install command (Admin PowerShell): `_____`

**B4.** In a WSL terminal, `~` means your Linux _____ folder.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. WSL + Ubuntu required.*

1. From PowerShell, show installed distros and their state with one command.
2. Enter Linux, and create `~/test1/` with a file `status.txt` containing `WSL works`.
3. Install `tree`, then use it on your home folder.
4. Create a file **on your Windows Desktop from inside WSL** (`from-wsl.txt`).
5. From **Windows Explorer**, navigate to your Linux home via `\\wsl$\...` and confirm `test1/status.txt` is visible.

**Extension (3 pts):** run `cat /etc/os-release | head -2` — write down the distro name and version, and explain what the `|` did (pipe: output of one command becomes input of the next).

### Rubric
| Points | Standard |
|---|---|
| 12 | All five steps done; both worlds accessed correctly |
| 5 | You can explain the interop paths (`/mnt/c`, `\\wsl$`) and why `sudo` asks for the Linux password |
| 3 | Extension completed with correct `|` explanation |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner keeps their Linux project in `/mnt/c/Users/me/projects` and complains builds are "weirdly slow" inside WSL.

**D2.** A tutorial says "run `sudo apt update`," a learner does it in **PowerShell** — and gets `'apt' is not recognized`.

---

## Part E — Apply & extend (6 pts)

A teammate asks why a developer on Windows would bother with WSL at all ("just use PowerShell"). In **4–6 sentences**, give **three** concrete reasons from the lesson — including at least one thing PowerShell genuinely cannot offer.

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

**A1.** Run a real Linux environment on Windows; WSL does it integrated and near-native instead of a heavyweight VM. · **A2.** `/mnt/c/...` (e.g., `/mnt/c/Users/<name>/Desktop`); `\\wsl$\Ubuntu\home\<name>`. · **A3.** Runs the command as administrator (superuser); asks for your **Linux** user password set during install. · **A4.** A flavor of Linux; Ubuntu (the friendly, best-documented default).
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `update` · **B2.** `install` · **B3.** `wsl --install` · **B4.** home
</details>

<details><summary><strong>Part C — grading notes</strong></summary>

Step 1: `wsl --list --verbose`. Step 2: `mkdir ~/test1 && cd ~/test1 && echo "WSL works" > status.txt` (note the Linux-side home, per the lesson's performance rule). Step 4: `echo ... > /mnt/c/Users/<name>/Desktop/from-wsl.txt`. Step 5 tests the Explorer path `\\wsl$\Ubuntu\home\<name>` — the interop is the heart of WSL. Extension: Ubuntu name/version + correct pipe explanation.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: project files behind the `/mnt` boundary are slow (cross-OS file bridge). Fix: keep Linux projects in the Linux home `~/`, visit `/mnt/c` only to reach Windows files. · **D2.** Bug: wrong world — `apt` is a Linux command, PowerShell is Windows. Fix: run it inside WSL (`wsl` first), and always check which side a tutorial's commands belong to (prompt shows it: `you@machine:~$` vs `PS C:\...`).
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

(1) Real Linux: `apt` package management, Linux tooling, dotfiles; (2) compatibility with the professional world — servers, containers, CI-CD runners, most tutorials are Linux-first; (3) the interop superpower — edit in Windows apps, run in Linux (PowerShell has no `/mnt/c`↔Linux-bridge equivalent or apt). Bonus: same Terminal First Lesson skills transfer directly.
</details>
