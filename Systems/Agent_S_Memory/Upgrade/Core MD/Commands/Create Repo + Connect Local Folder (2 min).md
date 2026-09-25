---
modified: 2026-04-23T20:35:17+03:00
---
Classic dev tax 😄 Here's the cheat sheet — commit it to memory:

---

## Create Repo + Connect Local Folder (2 min)

### Step 1 — Create repo on GitHub
Go to **github.com/new** → name it → **do NOT check** "Add README" → Create

### Step 2 — In your local AAT folder
```bash
cd /path/to/your/AAT-folder

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

That's it. Done.

---

### The one thing people always forget:
**Don't initialize with a README on GitHub** — if you do, the push fails because of divergent histories. Either skip it, or add `--force` to the push (messy).

---

### Bonus — if you already have a remote set from a previous project:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

---

Want me to also generate a solid `.gitignore` for a Python SDK project while we're at it? I can have that ready the moment you tell me the 3 answers from before.