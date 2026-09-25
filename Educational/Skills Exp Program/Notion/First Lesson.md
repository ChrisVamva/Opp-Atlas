# First Lesson — Notion

> **Welcome!** Notion is a workspace that behaves like LEGO for information: pages, blocks, and databases that snap together — notes that can hold tables, tables that can hold files, everything linkable. Today you'll learn its three building blocks and construct your first personal dashboard. By the end you'll understand why some people run their entire life and business inside it.

---

## 1. Why learn this?

- One tool replaces a mess of separate apps: notes app + to-do app + wiki + spreadsheet glue.
- Databases are Notion's superpower: the same information can appear as a table, a board, a calendar, or a gallery — switch views, same data.
- It's free for personal use and the skills transfer everywhere (many companies live in Notion).

**Where the other lessons meet this one:** [n8n](../n8n/First%20Lesson.md) can write into Notion databases automatically; [product creator](../product%20creator/First%20Lesson.md) and [Content Creation](../Content%20Creation/First%20Lesson.md) work both make great Notion dashboards for planning.

---

## 2. Prerequisites

- A browser and a free account: **notion.so** → sign up (email is fine).
- Nothing to install (apps exist for desktop/mobile, but the browser version is fully capable).

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | Tour: sidebar, pages, blocks |
| 10–25 min | Blocks: the atoms of Notion |
| 25–50 min | Databases: Notion's superpower |
| 50–70 min | Build your first dashboard |
| 70–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 Everything is a block
On a Notion page, every paragraph, heading, bullet, image, checkbox — even a whole embedded database — is a **block**. Type `/` (slash) to open the block menu: `/heading 1`, `/to-do list`, `/divider`, `/toggle`. Blocks can be dragged (grab the ⋮⋮ handle) to rearrange a page in seconds. This is why Notion feels like LEGO.

### 4.2 Pages nest inside pages
A page can contain sub-pages, which contain sub-pages... A **wiki** is just a well-organized nest. Keep nesting shallow (2–3 levels) — deep nests become where information goes to hide.

### 4.3 Databases: smart tables
A **database** is a table of **items** (rows), each with **properties** (columns): Text, Number, Select, Date, Checkbox, Person, Files. Example: a *Books* database with Name, Status, Rating, Finished-on.

The magic: **views**. The same data can display as a **Table**, **Board** (kanban with cards grouped by a Select property, like Status), **Calendar** (by a Date property), or **Gallery** (cards with covers). Not copies — one dataset, many lenses.

### 4.4 Filters and sorts: ask questions of your data
Views can filter and sort: "show only Books where Status = Reading, sorted by Rating descending." You're building little queries without knowing it.

### 4.5 Templates are starting points
Databases and pages can be duplicated from community templates (many free). Professionals rarely start from a blank page — they remix. That's allowed and encouraged.

---

## 5. Hands-on exercise

**Step 1 — Make your home page (10 min).** In the sidebar: **+ Add a page**. Name it **Dashboard**. Add blocks:
- `/heading 1` → "🏠 My Dashboard"
- `/divider`
- a `/callout` block → "Welcome to my workspace"

**Step 2 — Build the Books database (20 min).** Type `/table` → **Table – Full page** → name it **Books**. Add properties (click `+` right of the title column):

| Property | Type | Purpose |
|---|---|---|
| Name | Title (default) | book title |
| Status | Select | options: `Want to read` / `Reading` / `Finished` |
| Rating | Number | 1–5 |
| Finished | Date | completion date |

**Step 3 — Add three books (5 min).** Fill in three real books — one per status. Set a rating and a date on the finished one.

**Step 4 — Add a Board view (10 min).** Top-left of the database: **+ New view** → **Board** → group by **Status**. Drag one card between columns. Watch the Select property change itself. One dataset, two lenses — that's the core Notion trick, and you've done it.

**Step 5 — Filter a view (10 min).** On the Table view: **Filter** → Status is **Reading**. Now the table only shows what you're currently reading. Add **Sort** by Rating, descending. (You just built a query. Tell your friends you query databases now.)

**Step 6 — Assemble the dashboard (10 min).** Back on your **Dashboard** page, type `/linked view of database` → choose **Books**. Choose the Board view. Now your dashboard shows the live board — edit the database, the dashboard updates. Add a `/to-do list` block under it with 3 checkboxes.

**Expected result:** a Dashboard page containing a live Books database with Table + Board views, a filtered "Reading" view, and a to-do list — your first workspace, built by you.

---

## 6. Cheat sheet

| Thing | How |
|---|---|
| New page | sidebar `+ Add a page` |
| Any block | type `/` → pick from menu |
| Move a block | drag the ⋮⋮ handle |
| New database | `/table`, `/board`, `/calendar` (full page) |
| New property | `+` at the right end of the header row |
| New view | top-left of database: `+ New view` |
| Kanban | Board view grouped by a Select property |
| Filter | view menu → Filter → condition |
| Sort | view menu → Sort → property + direction |
| Live embed | `/linked view of database` on any page |
| Everything free plan | yes, for personal use — limits only on uploads/guests |

---

## 7. Common beginner mistakes

1. **Building page-after-page instead of databases.** If you find yourself re-typing the same structure (ten project pages with identical headings), you wanted a database with ten rows.
2. **Deep nesting chaos.** Pages inside pages inside pages... after 3 levels, information disappears. Flatten with linked views on one dashboard instead.
3. **One view per database.** Multiple views are the point — Table for editing, Board for status, Calendar for dates.
4. **Skipping properties.** A database with only a Title column is a list, not a database. Properties are what make views/filters/sorts possible.
5. **Template hoarding.** Duplicating ten elaborate templates you'll never fill. Start with one, customize ruthlessly.

---

## 8. Check yourself

1. What is a block and how do you open the block menu?
2. What's the difference between a database and a view?
3. In the Books database, what property type makes a kanban board possible?
4. What does a linked view of a database do?
5. You notice you're maintaining three separate pages with identical structure. What's the Notion answer?

<details><summary><strong>Answers</strong></summary>

1. Any piece of content on a page (paragraph, heading, to-do...). Type `/` to open the block menu.
2. A database holds the items+properties; a view is one lens on that data (table/board/calendar/gallery).
3. A **Select** property (like Status) — board columns are its options.
4. It embeds a live, editable copy of that database on another page; edits sync everywhere.
5. Convert to a database: one dataset, properties, views/filters — and one linked view on your dashboard.
</details>

---

## 9. Homework & what's next

**This week's homework:** build a **Habit Tracker** database on your own: Name, a Select "Category", seven Checkbox properties (Mon–Sun), and a Board view grouped by Category. Add five habits. Bonus: a filtered view showing only this week's un-checked habits.

**Lesson 2 preview:** relations & rollups (link Books ↔ Authors), formulas, and recurring-task templates — the features that make Notion feel like a custom app.

**Where to go next in this collection:** [n8n](../n8n/First%20Lesson.md) can write items into your Books database automatically; [product creator](../product%20creator/First%20Lesson.md) uses dashboards like today's for product planning.
