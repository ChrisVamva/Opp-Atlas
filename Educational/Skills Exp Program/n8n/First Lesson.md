# First Lesson — n8n

> **Welcome!** n8n (pronounced "n-eight-n") is a tool for building **automations**: little robots that watch for something happening and then do a series of tasks for you — no code required, though code is welcome. Today you'll install n8n free on your own machine and build a working two-node workflow that reads your mind's to-do list... almost. Let's start smaller: a robot that fetches data and hands it to you, automatically.

---

## 1. Why learn this?

- Repetitive digital chores — "check this site, save new items to a sheet, message me" — are exactly what n8n eats for breakfast.
- It's the middle path between no-code tools (Zapier) and full programming: visual enough for beginners, deep enough for professionals (self-hosted, unlimited runs, custom code when needed).
- Automation thinking — *inputs → logic → outputs* — upgrades how you approach every other skill in this collection.

**Where the other lessons meet this one:** [APIs](../APIs/First%20Lesson.md) taught you that data lives behind URLs; n8n is a visual way to consume them. [Python](../Python/First%20Lesson.md)/[Terminal](../Terminal/First%20Lesson.md) skills help when you self-host.

---

## 2. Prerequisites

- A computer with internet.
- **Node.js** (free, nodejs.org — install the LTS version). n8n runs on it. (If Node.js scares you, the lesson notes a no-install option below.)
- About 75 quiet minutes.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | The automation mindset: triggers and actions |
| 10–20 min | Install and launch n8n |
| 20–40 min | Build a first two-node workflow |
| 40–55 min | Add a branch: only act on some data |
| 55–70 min | Explore the template library |
| 70–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 Workflows are diagrams of "when X, then Y"
Every n8n workflow is a canvas of **nodes** connected by lines. Data flows left to right, transformed at each stop.

### 4.2 Every workflow starts with a trigger
A **trigger node** is the "when": an email arrives, a schedule fires (every morning), a webhook is hit, a form is submitted. No trigger, no run. The two you'll use today: **Schedule Trigger** ("run every day at 9:00") and **Manual Trigger** ("run when I click").

### 4.3 Action nodes do the work
After the trigger, **action nodes** do things: fetch a URL, filter, transform data, send a message, write to a sheet. Each node takes input data, does one job, passes its output to the next node. Chains of nodes = pipelines of logic.

### 4.4 Data moves as items
Nodes pass **items** — little JSON records — down the line. The HTTP Request node might output 10 items; a filter might let 2 through; the next node runs once per item. Think of items as letters on a conveyor belt.

### 4.5 Expressions: injecting live data into text
Anywhere a node has a field, you can click it and write an **expression** — a snippet that pulls a value from an earlier node, like `{{ $json.title }}`. That's how node B "knows" what node A found. (Syntax comes later; today you'll click rather than type expressions.)

---

## 5. Hands-on exercise

**Step 1 — Install and launch (10 min).**

Easiest free option: install **Node.js LTS** from nodejs.org, then open a terminal ([Terminal First Lesson](../Terminal/First%20Lesson.md) if needed) and run:

```
npx n8n
```

First run downloads n8n (~a minute). When you see `Editor is now accessible via: http://localhost:5678`, open that address in your browser. You're in the n8n editor. (No-install alternative: sign up free at n8n.cloud and follow along in the cloud editor.)

**Step 2 — Understand the canvas (5 min).** Click **Add workflow**. Empty canvas. Left sidebar = list of every integration (hundreds). The `Tab` key or the `+` opens the node search. Everything you build today is: **+ → search node → configure → connect**.

**Step 3 — Build workflow #1: Daily RSS digester (20 min).**

Goal: every morning, fetch the newest posts from a blog feed and hand them to you cleanly.

1. Add a **Schedule Trigger** node. Set it to fire, say, every day at 9:00.
2. Add an **RSS Read** node (search "RSS"), connect it after the trigger. Set URL to a blog feed, e.g. `https://hnrss.org/frontpage` (Hacker News front page).
3. Click **Execute workflow** (bottom). Watch items flow: the RSS node outputs one item per post.
4. Click the RSS node and inspect its **output**: JSON items with `title`, `link`, `pubDate`. You're reading API-style JSON — see the [APIs First Lesson](../APIs/First%20Lesson.md).
5. Save the workflow. Name it "Morning digest".

**Step 4 — Add a filter: be picky (15 min).** You don't want *all* posts, just interesting ones.

1. Add a **Filter** node between RSS and the end. Condition: `title` **contains** a keyword you care about (try `ai`).
2. Execute again. Fewer items survive. That's logic without code.
3. (Optional) Add an **Edit Fields (Set)** node to keep only `title` and `link`.

**Step 5 — Make it notify you (optional but magic).** Add a final node like **Gmail** (send yourself an email), **Telegram**, or **Discord** — connect your account when the node asks (free accounts work). Now the workflow is a real robot: *every morning, filter HN for `ai`, email me the hits.*

**Step 6 — Explore templates (10 min).** In the editor, open **Templates** and browse. Find one you like and read it like a diagram: trigger → steps. You'll be surprised how much you now understand.

**Expected result:** one saved working workflow (Schedule → RSS → Filter → [notification]), built and executed by you, plus one template you can now read.

---

## 6. Cheat sheet

| Term | Meaning |
|---|---|
| Workflow | the diagram of your automation |
| Node | one step (trigger, action, or logic) |
| Trigger | the "when" that starts every run |
| Item | one record flowing between nodes (JSON) |
| Expression | `{{ $json.fieldName }}` — pull a value from a previous node |
| Filter node | let only matching items through |
| Schedule Trigger | run on a clock ("daily at 9:00") |
| Manual Trigger / Execute | run now, for testing |
| HTTP Request node | talk to *any* API (the universal node) |
| localhost:5678 | n8n's editor address when self-hosted |

---

## 7. Common beginner mistakes

1. **Testing with the real trigger.** While building, use **Execute workflow** (manual) — don't wait for the 9:00 schedule to learn your filter is wrong.
2. **Forgetting to activate.** A saved workflow with the toggle **off** never runs. Toggle **Active** when it's ready for the real world.
3. **Connecting nodes in the wrong direction.** Data flows left→right along the arrows. A line backwards means "my output goes nowhere."
4. **Building monsters first.** Start with 2–3 nodes that work, then add. Debug one node at a time: click a node, read its input and output panels.
5. **Fear of expressions.** The `{{ $json.title }}` syntax is just JSON path-poking — click the field, drag tokens, let the editor write it.

---

## 8. Check yourself

1. What are the two jobs of any workflow's first node, and what happens without it?
2. In n8n terms, what is an "item"?
3. What does the expression `{{ $json.title }}` do?
4. You built a filter for posts containing "ai" but all items vanished. What are two likely causes?
5. What's the universal node for talking to *any* API?

<details><summary><strong>Answers</strong></summary>

1. The trigger starts the run; without a trigger (or manual execution) the workflow never fires.
2. One JSON record passed between nodes; a node's output is often many items, processed one-by-one downstream.
3. It injects the `title` field of the current item, taken from the previous node's output.
4. The condition is too strict or case-sensitive (try "contains, case-insensitive"), or the feed simply has no matching posts today — test with a broader keyword.
5. The **HTTP Request** node.
</details>

---

## 9. Homework & what's next

**This week's homework:** build a second workflow end-to-end on your own: **Schedule → HTTP Request** to a free public API (e.g., `https://api.open-meteo.com/v1/forecast?latitude=38.7&longitude=-9.1&current_weather=true` — see [APIs First Lesson](../APIs/First%20Lesson.md)) **→ Filter** for temperature above/below a threshold **→ email/Telegram yourself**. "Email me if it will be hot tomorrow" is a genuinely useful first robot.

**Lesson 2 preview:** expressions in depth, error handling (what happens when an API fails?), and webhooks — workflows that run when *outside services* call *you*.

**Where to go next in this collection:** [APIs](../APIs/First%20Lesson.md) (understand what the HTTP node is really doing), [Notion](../Notion/First%20Lesson.md) (a favorite n8n destination for storing what robots find), and [vector databases](../vector%20databases/First%20Lesson.md) (advanced robots do AI search — n8n has nodes for that too).
