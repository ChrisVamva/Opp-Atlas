# Test1 — Notion

> **When:** after the [First Lesson](First%20Lesson.md) and its Habit Tracker homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What is a block, and how do you open the block menu?

**A2.** What's the difference between a database and a view?

**A3.** Which property type powers a kanban board, and why?

**A4.** You're maintaining three pages with identical structure. What's the Notion answer — and what's the 3-level nesting rule for?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Open the block menu by typing `_____` on an empty line.

**B2.** Make the same database appear live on another page: `_____ view of database`.

**B3.** Group a Board by a `_____` property (like Status).

**B4.** Show only "Reading" books: add a `_____` to the view.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Your Notion workspace.*

Build a **Job Applications tracker** (new domain — tests transfer, not memory):

1. Full-page database with properties: **Company** (Title), **Status** (Select: `Applied` / `Interview` / `Offer` / `Rejected`), **Applied on** (Date), **Priority** (Number).
2. Add four real-ish rows, one per status.
3. Add a **Board view** grouped by Status; drag one card between two columns and record what changed.
4. On the Table view: **filter** to `Interview` only, **sort** by Priority descending.
5. On your Dashboard page (from the lesson), embed a **linked view** of this database.

**Extension (3 pts):** add a `Salary expectation` (Number) property and a second Table view showing only offers, sorted by salary descending — then explain in one sentence why that's a *new view*, not a new database.

### Rubric
| Points | Standard |
|---|---|
| 12 | Database with all four properties; board drag demonstrated; filter + sort on table; linked view on Dashboard |
| 5 | You can explain views vs. databases and why the board needs a Select |
| 3 | Extension: new view + correct one-dataset reasoning |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner creates a *new page* for every job application, each with the same headings — and can't answer "how many am I waiting on?"

**D2.** A learner's Board shows one giant column "Uncategorized" — the Status property exists but the board won't group.

**D3.** *(Bonus scenario, not scored separately)*: a learner drags a card to a new column, then the card "loses" its status — what actually happened?

---

## Part E — Apply & extend (6 pts)

A friend tracks workouts in ten separate notes. In **4–6 sentences**, explain what you'd build instead — using the lesson's terms: **database**, **properties**, **views**, and name one view type that would help them and why.

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

**A1.** Any piece of content on a page (paragraph, heading, to-do, embedded database); type `/` to open the block menu. · **A2.** A database stores items + properties (the data); a view is one lens on it (Table/Board/Calendar/Gallery) — same dataset, many displays. · **A3.** Select — board columns are that property's options; dragging a card changes the Select value. · **A4.** Convert to one database with views/filters (one dataset). Nesting rule: keep pages 2–3 levels deep — deeper, and information hides.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `/` · **B2.** `linked` · **B3.** Select · **B4.** filter
</details>

<details><summary><strong>Part C — grading notes</strong></summary>

New domain (job apps) tests transfer of: properties as types, board = Select-driven, filter/sort per view, linked view = live embed. The recorded drag is the graded proof that board columns *are* the Select options. Extension reasoning: new view reuses the same dataset; a new database would duplicate data and split truth.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: page-per-item instead of database rows — identical structure repeated means a database was wanted (properties, views, counts). Fix: one database, one row per application. · **D2.** Bug: Board not grouped by the Select property. Fix: view settings → Group by → Status. · **D3.** (bonus) Nothing lost — the drag *set* Status to the new column's option; the old value was replaced by design.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

One **database** (one row per workout) with **properties** (date, type, duration, distance...); **views** answer different questions without duplicating data — e.g., a Calendar view (see workouts across the month) or a Board grouped by workout type. Killer argument: ten notes can't filter, sort, or count; a database answers "how many runs this month?" instantly.
</details>
