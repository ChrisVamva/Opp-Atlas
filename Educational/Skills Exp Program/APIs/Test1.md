# Test1 — APIs

> **When:** after the [First Lesson](First%20Lesson.md) and its PokéAPI homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** In the restaurant analogy, what are the waiter, the menu, and the kitchen?

**A2.** What's the difference between `{}` and `[]` in JSON, and what can appear inside each?

**A3.** You get a **429**. What does it mean and what do you do?

**A4.** Why is one page = one primary keyword the rule in SEO, and how does the same discipline apply to APIs? *(Think: what does one endpoint do?)*

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** The request verb for "give me data": `_____`

**B2.** Start the query parameters of a URL: `?`, separate multiple pairs with `_____`.

**B3.** Status `_____` means "not found — check the URL."

**B4.** In JSON, `"followers": 12` — `"followers"` is the _____, `12` is the _____.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Browser address bar is enough.*

1. Call `https://api.github.com/users/torvalds` — write down the `login`, `public_repos`, and `followers` values.
2. Call the repos endpoint for the same user. State whether the response is a `{}` or `[]`, and the `name` of the first repository.
3. Call Open-Meteo for Lisbon: `https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true` — write down `temperature` and `windspeed`.
4. Modify the same URL for New York (`latitude=40.71&longitude=-74.01`) — write down the new temperature.
5. Call `https://api.github.com/users/this-user-should-not-exist-98765` — record the status code and one line of the error body.

**Extension (3 pts):** add `hourly=temperature_2m` to the Lisbon Open-Meteo URL and extract the temperature at hour index 12 of `hourly.time`. Write down both the value and how you located it (the skill: reading *nested* JSON).

### Rubric
| Points | Standard |
|---|---|
| 12 | All five calls made; values correctly extracted; the 404 interpreted calmly and correctly |
| 5 | You can explain each URL's anatomy (endpoint, `?`/`&`, why parameters change the answer) |
| 3 | Extension completed |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner builds `https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14current_weather=true` and the response has no weather data.

**D2.** A learner calls `https://api.github.com/users/octocat` from a script and gets **401** — the same URL worked in the browser.

---

## Part E — Apply & extend (6 pts)

You want tomorrow's temperature for your city every morning without opening a browser. In **4–6 sentences**: which endpoint and parameters you'd use, how the URL changes per city, which status code you'd watch for if the API rate-limits you, and which two other skills from this collection would automate it.

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

**A1.** Waiter = the API carrying requests in/responses out; menu = the documentation (what may be ordered); kitchen = the server's data/logic you never touch directly. · **A2.** `{}` = object: labeled drawer of `key: value` pairs; `[]` = array: ordered list of values (objects, strings, numbers...). · **A3.** "Too many requests" — you're rate-limited: slow down / wait / authenticate. · **A4.** An endpoint has one focused job (like one page targets one keyword); mixing concerns into one call/keyword means serving neither well.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `GET` · **B2.** `&` · **B3.** `404` · **B4.** key; value
</details>

<details><summary><strong>Part C — grading notes</strong></summary>

Values change over time — grade the *extraction*, not the numbers: correct keys found (`login`/`public_repos`/`followers`; first repo's `name`; `current_weather.temperature`/`windspeed`), array vs. object correctly identified (`[]` for repos), 404 + JSON error message recorded. Step 4 tests that parameters — not the endpoint — change the answer. Extension: nested reading, `hourly.time[12]` paired with `hourly.temperature_2m[12]`.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: missing `&` before the second parameter — `...-9.14current_weather=true` reads as one malformed value. Fix: `&current_weather=true`. · **D2.** Bug: unauthenticated requests to api.github.com are rate-limited per IP; the script exhausted the limit. Fix: slow down/back off, and (Lesson 2 preview) authenticate with a token — 401/403 signal missing auth.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

Open-Meteo forecast endpoint with their city's coordinates + `current_weather=true`; per-city change = only the two coordinate parameters; watch for **429** when polling often; automation via **n8n** (Schedule Trigger → HTTP Request → notification) or **Python** (requests + a scheduler). Bonus: the pipeline shape from the vector-databases/APIs lessons (fetch → filter → act).
</details>
