# Test1 — JavaScript

> **When:** after the [First Lesson](First%20Lesson.md) and its mini-app homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What's the difference between `let` and `const`?

**A2.** Why does the lesson say to prefer `===` over `==`?

**A3.** In the mini-app, what are `document.getElementById(...)` and `.innerText` for?

**A4.** What is the console's job in your workflow (name two uses)?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** `"5" + 5` evaluates to `_____`.

**B2.** The keyword that creates a box which can never be reassigned: `_____`.

**B3.** Grab the element with `id="title"`: `document._____("title")`.

**B4.** Print for humans: `console._____("hi")`.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Start from the mini-app from the lesson, in a browser.*

Extend the mini-app so that:

1. The button handler reads the name **and** checks it isn't empty (empty → message "Please type a name").
2. When a name is present: the `h1` becomes `Hi, <name>!` and the paragraph reports the **length** of the name (e.g., "That's 5 characters long.").
3. Add a second button, **Reset**, that clears the input and restores the original `h1` text.

**Extension (3 pts):** make the greeting uppercase on the button click (e.g., `HI, MAYA!`) and explain in one comment *why* `"5" + 5` is `"55"`.

### Rubric
| Points | Standard |
|---|---|
| 12 | All three behaviors work after refresh; empty case handled |
| 5 | You can explain the DOM calls used, per line |
| 3 | Extension working + comment present |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner writes `if (name = "") { ... }` inside `sayHi()` — the branch runs *always*, and the input gets erased on every click.

**D2.** A learner calls `document.getElementByID("output")` — and nothing happens; the console shows `...getElementByID is not a function`.

**D3.** *(Bonus scenario, not scored separately)*: `let city = Lisbon` crashes with "Lisbon is not defined" — why?

---

## Part E — Apply & extend (6 pts)

A friend asks: "Why do web pages need JavaScript at all — isn't HTML enough?" In **4–6 sentences**, answer using the lesson's terms: **DOM**, *behavior vs. appearance*, and one example from your own mini-app (name the event that triggered your code).

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

**A1.** `let` creates a reassignable box; `const` creates one that can't be reassigned (prefer it when the value won't change). · **A2.** `===` compares value **and** type; `==` does sneaky type conversion, which causes subtle bugs. · **A3.** `getElementById` finds an element in the page's DOM; `.innerText` reads/changes the visible text of that element. · **A4.** Run/see code instantly and `console.log` for debugging; read error messages (with line numbers) when code fails.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `"55"` · **B2.** `const` · **B3.** `getElementById` · **B4.** `log`
</details>

<details><summary><strong>Part C — model solution</strong></summary>

```javascript
function sayHi() {
  const box = document.getElementById("nameBox");
  const name = box.value;

  if (name === "") {
    document.getElementById("output").innerText = "Please type a name";
  } else {
    document.getElementById("title").innerText = "Hi, " + name + "!";
    document.getElementById("output").innerText =
      "That's " + name.length + " characters long.";
  }
}

function resetApp() {
  const box = document.getElementById("nameBox");
  box.value = "";
  document.getElementById("title").innerText = "Hello, stranger";
  document.getElementById("output").innerText = "";
}
```

HTML additions:
```html
<button onclick="resetApp()">Reset</button>
```

Model extension: `document.getElementById("title").innerText = "HI, " + name.toUpperCase() + "!";` — and the comment: `"5" + 5` is `"55"` because when either side of `+` is a string, JavaScript converts the number to text and glues them (string wins).
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: `=` **assigns** (writes `""` into `name`, which is falsy → the branch runs every time) instead of **comparing**. Fix: `if (name === "")`. · **D2.** Bug: case-sensitivity — the method is `getElementById` (lowercase "by"). Fix: exact casing; remember JS is case-sensitive everywhere. · **D3.** (bonus) Quotes were forgotten: without them, `Lisbon` is treated as a variable name that doesn't exist.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

HTML is the static *appearance* (structure); JavaScript is the *behavior* — it reads/changes the DOM in response to events. Concrete example from their mini-app: the button click (the event) ran `sayHi()`, which changed the `h1` and paragraph via `getElementById`/`innerText`. Extra credit: pages can also react without reloads because JS edits the live DOM.
</details>
