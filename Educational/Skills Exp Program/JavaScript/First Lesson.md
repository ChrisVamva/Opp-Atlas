# First Lesson — JavaScript

> **Welcome!** JavaScript is the programming language of the web — every button you click, every page that updates without reloading, every online form: that's JavaScript running in your browser. Today you will write your first code inside the browser you already have, and make a web page react to you. No installs, no accounts — your browser *is* the classroom.

---

## 1. Why learn this?

- It's the only language every web browser understands, which makes it the fastest path from "code" to "something I can see and touch."
- One language covers websites, browser tools, and (with Node.js) servers too — hugely versatile.
- The feedback loop is instant: type code, see the effect on screen immediately. Perfect for beginners.

**Where the other lessons meet this one:** [Web Design](../Web%20Design/First%20Lesson.md) teaches how pages *look* (HTML/CSS); JavaScript teaches how they *behave*. [APIs](../APIs/First%20Lesson.md) + JavaScript is how websites pull live data. Python (see [Python](../Python/First%20Lesson.md)) is its friendlier cousin for non-web work.

---

## 2. Prerequisites

- A web browser — Chrome, Edge, or Firefox. That's genuinely all.
- Today happens entirely in the browser's **developer console**. If you've never opened it:
  - **Chrome/Edge:** press `F12` (or `Ctrl + Shift + J` / `Cmd + Option + J` on Mac), then click the **Console** tab.
  - **Firefox:** press `F12`, click **Console**.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | Open the console, say hello |
| 10–30 min | Variables, types, and math |
| 30–45 min | Functions and strings |
| 45–65 min | First interactive page: a live mini-app |
| 65–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 Code runs top to bottom
Just like [Python](../Python/First%20Lesson.md), the computer reads your instructions in order and does exactly what they say, instantly. In the console, each `Enter` executes the line.

### 4.2 Variables hold values
```javascript
let city = "Lisbon";
let temperature = 24;
```
`let` declares ("creates") a box with a label. Change it later with `city = "Porto";`. (You'll also see `const` — a box that can never be reassigned. Prefer it when the value won't change.)

### 4.3 Types: strings, numbers, booleans
- **string:** text — `"hello"` (single or double quotes both fine).
- **number:** `42` or `3.14` — one type for all numbers.
- **boolean:** `true` / `false` — the on/off switch of all logic.

### 4.4 Functions are reusable recipes
```javascript
function greet(name) {
  return "Hello, " + name + "!";
}
```
Define once, use everywhere: `greet("Maya")` gives `"Hello, Maya!"`. The `return` sends a value back to whoever called the function.

### 4.5 The DOM: JavaScript's hands on the page
The browser keeps a live model of the page called the **DOM** (Document Object Model) — think of it as the page's scaffolding. JavaScript reads and changes it: find an element, change its text, react when it's clicked. That's the whole trick behind "interactive."

---

## 5. Hands-on exercise

**Part A — Console warm-up (15 min)**

Open the console. Type each line, predict the result, press Enter:

```javascript
2 + 2
"2" + "2"
"2" + 2          // surprise! strings win
let city = "Lisbon"
city
city.toUpperCase()
city.length
Math.max(3, 99, 42)
let lucky = 7
lucky * 6
console.log("Console says hi")
```

Notes: `//` starts a comment (ignored by the computer). `console.log(...)` prints things — your best debugging friend. `"2" + 2` shows JavaScript's famously quirky side: when you glue a string to a number, the number becomes text (`"22"`). Keep that in your pocket; it explains many future bugs.

**Part B — A function (10 min)**

```javascript
function greet(name) {
  return "Hello, " + name + "! Welcome to JavaScript.";
}
greet("Maya")
greet("world")
```

Make a second function `shout(text)` that returns the text in UPPERCASE with an exclamation mark (hint: `text.toUpperCase() + "!"`). Test it.

**Part C — Your first interactive page (25 min)**

**Step 1.** Open a plain-text editor and save this as `mini-app.html`:

```html
<!DOCTYPE html>
<html>
  <body style="font-family: sans-serif; max-width: 420px; margin: 60px auto;">
    <h1 id="title">Hello, stranger</h1>
    <input id="nameBox" placeholder="Type your name">
    <button onclick="sayHi()">Greet me</button>
    <p id="output"></p>

    <script>
      function sayHi() {
        const box = document.getElementById("nameBox");
        const name = box.value;

        if (name === "") {
          document.getElementById("output").innerText =
            "You forgot to type a name!";
        } else {
          document.getElementById("title").innerText = "Hi, " + name;
          document.getElementById("output").innerText =
            "The page now knows your name, " + name + ".";
        }
      }
    </script>
  </body>
</html>
```

**Step 2.** Double-click the file to open it in your browser.

**Step 3.** Type a name, press **Greet me**. The heading and message change — *that* is JavaScript controlling the DOM. Try the empty-input case too: the `if/else` handled it.

**Step 4 — Make it yours.** Add a second button that clears the input and resets the title to "Hello, stranger" (hint: `box.value = ""` and set `innerText` again). Add one more line to the message using `.toUpperCase()` somewhere.

**Expected result:** a small web page that responds to your input, built and extended by you — no installs, no accounts.

---

## 6. Cheat sheet

| Thing | Example | Meaning |
|---|---|---|
| Declare | `let x = 5` / `const y = 10` | mutable box / fixed box |
| String | `"hi"` or `'hi'` | text |
| Concatenate | `"a" + "b"` | `"ab"` (numbers become text!) |
| Length | `city.length` | number of characters |
| Uppercase | `city.toUpperCase()` | `"LISBON"` |
| Function | `function f(a) { return a }` | reusable recipe |
| Print | `console.log(x)` | show in console |
| If/else | `if (x === 5) { ... } else { ... }` | decisions |
| Strict equal | `===` | compare value *and* type — prefer over `==` |
| Find element | `document.getElementById("id")` | grab a page element |
| Set text | `el.innerText = "new"` | change what's displayed |
| Open console | `F12` → Console | your lab |

---

## 7. Common beginner mistakes

1. **`=` vs `===`.** `=` assigns (`x = 5` puts 5 in the box); `===` compares (`if (x === 5)`). Mixing them is the classic beginner bug.
2. **Capitalization.** `getElementByID` fails silently in your head and loudly on screen — it's `getElementById`. JavaScript is case-sensitive everywhere.
3. **Forgetting the quotes.** `let city = Lisbon` means "a variable named Lisbon" (error). Text needs quotes.
4. **Editing the file but not refreshing.** After changing `.html`, save and press `F5` in the browser.
5. **Panicking at a red error.** The console error tells you the line number — read it, fix, re-run. Errors are instructions, not verdicts.

---

## 8. Check yourself

1. What does `let` do, and how is `const` different?
2. What is `"5" + 5` in JavaScript, and why?
3. In the mini-app, what does `document.getElementById("title")` find?
4. Why do we use `===` instead of `==`?
5. You changed the HTML file but the browser shows the old version. What happened?

<details><summary><strong>Answers</strong></summary>

1. `let` creates a variable you may reassign; `const` creates one that can't be reassigned.
2. `"55"` — when one side is a string, JavaScript converts the number to text and glues them.
3. The heading element `<h1 id="title">` — the DOM node for that heading.
4. `===` compares value and type, avoiding sneaky conversions that `==` allows.
5. You didn't save the file, or didn't refresh the page (`F5`) — or you're looking at a different file.
</details>

---

## 9. Homework & what's next

**This week's homework:** extend the mini-app into a tiny **mad-skill generator**: add an input for a skill and a number input (hint: `<input type="number">`), and have the button print "In N months you'll be great at SKILL." Bonus: make the greeting function come from Part B and reuse it.

**Lesson 2 preview:** arrays (lists), loops, and click-handlers on multiple buttons — the building blocks of real pages.

**Where to go next in this collection:** [Web Design](../Web%20Design/First%20Lesson.md) (make that page beautiful with CSS), [APIs](../APIs/First%20Lesson.md) (feed your page live data from the internet), and [Terminal](../Terminal/First%20Lesson.md) when you're ready for Node.js on your machine.
