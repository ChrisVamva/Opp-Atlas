# First Lesson — Web Design

> **Welcome!** Web design is deciding how a web page *looks and feels* — what goes where, how big the headline is, which colors talk and which stay quiet. Today you'll learn the handful of rules that separate amateur pages from professional ones, and you'll design (and improve) a real page yourself. No code required today, though we'll peek at how the code connects.

---

## 1. Why learn this?

- Everyone can *make* a page (tools make it easy); few can make one that looks *right*. That gap is a superpower.
- Design is not decoration — it's communication. Good design tells the visitor where to look and what to do next, without a word.
- These rules transfer to everything visual: slides, posters, dashboards, resumes, [product landing pages](../product-marketing%20skills/First%20Lesson.md).

**Where the other lessons meet this one:** [JavaScript](../JavaScript/First%20Lesson.md) makes pages behave; this one makes them look right. [Content Creation](../Content%20Creation/First%20Lesson.md) and [SEO](../SEO/First%20Lesson.md) both benefit from pages people actually enjoy reading.

---

## 2. Prerequisites

- A browser, and eyes. That's it for today.
- Optional but recommended: a free Figma account (figma.com) if you'd rather sketch digitally than on paper.
- Paper and pen work perfectly too.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | Train your eye: compare good vs. bad pages |
| 10–30 min | The five core ideas (layout, hierarchy, type, color, space) |
| 30–50 min | Exercise 1: wireframe a page by hand |
| 50–70 min | Exercise 2: diagnose and fix a real page |
| 70–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 Layout: boxes in boxes
Every page — no matter how fancy — is **rectangles inside rectangles**. A header bar, a content column, cards inside a grid. Train yourself to *see* the boxes: open any site and squint until it's all gray rectangles. Design becomes much less scary when you see it's just boxes with intention.

### 4.2 Visual hierarchy: some things matter more
The page must answer, in order: *Where am I? What is this? What do I do next?* You control the answer with **size**, **weight**, **color**, and **position**. The most important element should be impossible to miss — usually a big headline and one obvious button. If everything shouts, nothing is heard.

### 4.3 Typography: two fonts are enough
- Pick **one font for headings**, **one for body** (when unsure: one family, two weights — e.g. Inter Regular + Inter Bold).
- Body text: 16–18px minimum, line-height about **1.5**, line length around **50–75 characters**. Longer lines tire the eye.
- Never underline text that isn't a link. All-caps for long text is hard to read.

### 4.4 Color: the 60-30-10 rule
- **60%** dominant (usually a near-white or near-black background),
- **30%** secondary (your brand color, section backgrounds),
- **10%** accent (buttons, links — the things that must get clicked).
Beginner palette formula: near-white background + near-black text + **one** saturated accent color. That's already professional.

### 4.5 Whitespace is not wasted space
Empty space is what makes content readable and pages feel calm. Cramped pages feel cheap; spacious ones feel trustworthy. When in doubt: **more padding**. Beginners consistently use half the whitespace they should.

---

## 5. Hands-on exercise

**Exercise 1 — Wireframe a page (20 min)**

A **wireframe** is a skeleton drawing: gray boxes where content will go, no colors, no fonts. On paper (or Figma), wireframe a simple **personal landing page** with:

1. A header row: name on the left, three nav links on the right
2. A hero section: one big headline, one sentence of subtext, one button
3. Three cards in a row (e.g., projects, skills, contact)
4. A simple footer

Rules: pencil/gray only. Label each box (e.g., "headline", "photo", "CTA" — call-to-action). Draw the *hierarchy*: which box is visually biggest? Mark your one accent element.

**Exercise 2 — Diagnose a page (20 min)**

Open a website you find ugly or hard to read (or build the tiny page from the [JavaScript First Lesson](../JavaScript/First%20Lesson.md) — it's deliberately plain). Using your five concepts, write down answers:

1. **Layout:** can you see the boxes? Is the structure aligned to a grid?
2. **Hierarchy:** what's the single most important element? Can you find the main button in 2 seconds?
3. **Typography:** how many fonts? Is body text ≥16px with breathing room?
4. **Color:** is there a clear 60-30-10? How many accent colors fight for attention?
5. **Whitespace:** which section feels cramped, and what one padding change would fix it?

Then fix the JavaScript lesson's page: add `max-width: 640px; margin: 0 auto;` to center content, increase body font to 17px, add one accent color to the button only, and add generous padding. Small changes, dramatic difference.

**Expected result:** a labeled wireframe on paper, a written 5-point diagnosis of a real page, and (optionally) one visibly improved HTML file.

---

## 6. Cheat sheet

| Concept | Quick rule |
|---|---|
| Layout | everything is boxes in boxes; align to a grid |
| Hierarchy | one hero element; size + weight + color = importance |
| Fonts | 1–2 families max; body 16–18px; line-height ~1.5 |
| Line length | 50–75 characters per line |
| Color | 60% neutral, 30% secondary, 10% accent |
| Accent | one color, reserved for buttons/links |
| Whitespace | when in doubt, add more padding |
| Squint test | blur your eyes; structure should still be obvious |
| Wireframe | gray boxes + labels, no styling |

---

## 7. Common beginner mistakes

1. **Too many fonts and colors.** Two fonts and three colors *is* a design system. Chaos is the default, restraint is the skill.
2. **Centering everything.** Centered text everywhere flattens hierarchy. Left-align body text; reserve centering for heroes.
3. **Low-contrast gray-on-gray text.** If it's hard to read, it *is* hard to read — accessibility is not optional.
4. **Skipping the wireframe.** Choosing colors before layout is painting a house you haven't built.
5. **Filling every pixel.** Fear of emptiness. Space signals confidence.

---

## 8. Check yourself

1. What are the five core concepts from today?
2. In 60-30-10, what goes in the 10% and why so little?
3. What's a wireframe and why come before colors?
4. Your page has 6 fonts and 4 accent colors. What's the fix?
5. What does the "squint test" check?

<details><summary><strong>Answers</strong></summary>

1. Layout, visual hierarchy, typography, color, whitespace.
2. The accent — buttons and links — because scarcity is exactly what makes those elements noticeable.
3. A gray-box skeleton of the page. Layout and hierarchy decisions come first; styling is easier and cheaper once structure is fixed.
4. Cut to max 2 font families and 1 accent color; let weight and size do the differentiating.
5. Whether the page's structure and hierarchy survive without detail — if it's a gray mush when blurred, hierarchy is missing.
</details>

---

## 9. Homework & what's next

**This week's homework:** every day, find one website and write a 2-line diagnosis (one strength, one fix) using the five concepts. By Friday, pick your best diagnosis and actually implement the fix — screenshot the before/after.

**Lesson 2 preview:** CSS fundamentals hands-on — the box model, flexbox for layout, and building the wireframe from today as a real page.

**Where to go next in this collection:** [JavaScript](../JavaScript/First%20Lesson.md) for behavior, [SEO](../SEO/First%20Lesson.md) for being found, and [product-marketing skills](../product-marketing%20skills/First%20Lesson.md) for pages whose whole job is to convert.
