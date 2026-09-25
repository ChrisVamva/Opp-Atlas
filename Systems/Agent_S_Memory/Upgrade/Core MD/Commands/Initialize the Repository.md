---
modified: 2026-04-16T07:07:57+03:00
---
## Process Overview

### Step 1: Initialize the Repository

```
git init
```

### Step 2: Configure Git (first-time setup)

```
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 3: Create a `.gitignore` File

Create a `.gitignore` to exclude files like `node_modules`, `.env`, and build artifacts.

### Step 4: Stage All Files

```
git add .
```

### Step 5: Make Initial Commit

```
git commit -m "Initial commit"
```

### Step 6: Create Remote Repository on GitHub

Go to [https://github.com/new](https://github.com/new) and create a new repository (or use the GitHub CLI if installed).

### Step 7: Connect Local Repo to GitHub

```
git remote add origin https://github.com/username/repo-name.git
```

### Step 8: Push to GitHub

```
git push -u origin main
```