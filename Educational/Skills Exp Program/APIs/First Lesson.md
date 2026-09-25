# First Lesson — APIs

> **Welcome!** An API (Application Programming Interface) is how programs talk to each other over the internet. When your weather app shows tomorrow's forecast, it asked a weather company's API for the data. Today you will make your first real API requests — and by the end you'll have pulled live data from the internet with your own hands, no code required.

---

## 1. Why learn this?

- Almost everything interesting on the internet is data from somewhere else: prices, weather, maps, AI models, sports scores. APIs are the taps.
- Once you can call an API, every programming skill becomes 10× more powerful — you're no longer limited to data you typed yourself.
- It demystifies the web: behind every app is a conversation, and you'll be able to listen in.

**Where the other lessons meet this one:** [Python](../Python/First%20Lesson.md) can automate API calls; [JavaScript](../JavaScript/First%20Lesson.md) is how web pages fetch live data; [n8n](../n8n/First%20Lesson.md) lets you build automations *out of* API calls without writing code.

---

## 2. Prerequisites

- A browser. Optional: [Terminal](../Terminal/First%20Lesson.md) comfort if you want to try the command-line route at the end.
- No installs, no accounts, no keys. We'll use free, open public APIs that require nothing.

---

## 3. Session roadmap (~75 minutes)

| Time | Activity |
|---|---|
| 0–10 min | The restaurant analogy: what an API really is |
| 10–25 min | URLs, requests, responses — and JSON |
| 25–45 min | Hands-on: real GET requests in the browser |
| 45–60 min | Read JSON like a pro; query parameters |
| 60–75 min | Quiz + homework |

---

## 4. Core concepts

### 4.1 The restaurant analogy
An API is a **waiter**. You (the client) don't walk into the kitchen (the server's database) — you tell the waiter what you want from the menu, the kitchen prepares it, and the waiter brings it back. The menu is the API **documentation**: it lists what you can order.

### 4.2 A request is just a URL
The simplest API call is a web address. When you go to:

```
https://api.github.com/zen
```

your browser makes a **GET request** ("give me something") and the server sends back a **response**. GET is the most common of a small family of verbs (GET = read, POST = create, PUT/PATCH = update, DELETE = delete — today we only use GET).

### 4.3 The response is usually JSON
**JSON** (JavaScript Object Notation) is the universal format for structured data — text that machines parse easily and humans can read with practice:

```json
{
  "name": "Maya",
  "age": 29,
  "skills": ["python", "apis"]
}
```

Rules: keys in double quotes, values can be text, numbers, booleans, arrays `[...]` (lists) or objects `{...}` (nested records). If JSON is a labeled filing cabinet, `{}` is a drawer and `[]` is a folder of items.

### 4.4 Status codes: the response's mood
Every response carries a 3-digit status code:
- **200** — success, here's your data.
- **404** — "I don't have that" (wrong address).
- **401/403** — "you're not allowed" (missing key or permission).
- **429** — "slow down" (too many requests).
- **500** — "it's not you, it's me" (server broke).

### 4.5 Query parameters customize the order
URLs can carry extra instructions after a `?`, as `key=value` pairs joined by `&`:

```
https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true
```

That's you telling the waiter: "forecast, for these coordinates, current weather only."

---

## 5. Hands-on exercise

Do these in your browser's address bar (yes, really). For each, *predict first*, then look at the response and find the status code (F12 → Network tab → click the request, or just read what you got).

**Request 1 — The simplest possible call**
```
https://api.github.com/zen
```
Expected: a short wisdom sentence as plain text. Status 200. You just made an API call.

**Request 2 — Your first JSON**
```
https://api.github.com/users/octocat
```
Expected: a JSON object about a GitHub user. Find: their `login`, `public_repos`, `followers`. You just *read* JSON.

**Request 3 — A list**
```
https://api.github.com/users/octocat/repos
```
Expected: a JSON *array* — `[]` containing many `{}` objects, one per repository. Count them. Find the `name` of the first one.

**Request 4 — Query parameters change the answer**
```
https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true
```
Expected: current weather for Lisbon. Find `temperature` and `windspeed` inside `current_weather`. Now change the coordinates: `latitude=40.71&longitude=-74.01` (New York). Same endpoint, different answer — parameters are how one API serves the whole world.

**Request 5 — Practice reading nested JSON**
```
https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true&hourly=temperature_2m
```
Find: the current temperature, then the temperature at hour index 12 of `hourly.time`. Nested data is just drawers inside drawers.

**Request 6 — A broken call (on purpose)**
```
https://api.github.com/users/this-user-should-not-exist-98765
```
Expected: status **404** and a JSON error message. Errors are normal, expected, and *informative* — the status code tells you the category of problem instantly.

**Expected result:** six real API calls made by you, JSON read fluently enough to pull specific values out, and one honest error handled calmly.

**Bonus (terminal route):** if you did the [Terminal First Lesson](../Terminal/First%20Lesson.md), try:
```
curl https://api.github.com/zen
```
Same request, different tool — APIs are program-agnostic.

---

## 6. Cheat sheet

| Term | Meaning |
|---|---|
| API | how programs talk to each other |
| Endpoint | the URL you call |
| GET | "give me data" (today's only verb) |
| JSON | text format for structured data: `{}` object, `[]` array |
| Key / value | `"name": "Maya"` — the label and its content |
| Query parameter | `?latitude=40&longitude=-74` — customize the request |
| Status 200 | success |
| Status 404 | not found — check the URL |
| Status 401/403 | not authorized — key/permission problem |
| Status 429 | too many requests — slow down |
| Status 5xx | server's fault — try later |

---

## 7. Common beginner mistakes

1. **Reading JSON like prose.** Scan the *structure* first: `{}` or `[]`? Then find the key you need. Top-down beats word-by-word.
2. **Blaming yourself for 4xx errors.** 404/401 mean *your request* needs fixing — that's good news, it's fixable. Only 5xx is the server's fault.
3. **Forgetting `?` and `&` syntax.** First parameter gets `?`, the rest get `&`. One typo and the server ignores your parameter.
4. **Trusting unauthenticated APIs for anything serious.** Public demo APIs can change or rate-limit you without notice. (Real apps use keys — that's Lesson 2.)
5. **Not reading the docs.** The "menu" tells you what's orderable. Two minutes in the docs saves twenty of guessing.

---

## 8. Check yourself

1. In the restaurant analogy, what are the waiter, the menu, and the kitchen?
2. What's the difference between `{}` and `[]` in JSON?
3. Write a URL that asks the GitHub API for user `torvalds`.
4. You get a 401. What does it mean and what's the likely fix?
5. In `?latitude=38.7&longitude=-9.1&current_weather=true`, what do `?` and `&` each do?

<details><summary><strong>Answers</strong></summary>

1. Waiter = the API (carries requests in, responses out). Menu = the documentation (what you may order). Kitchen = the server's data/logic you never touch directly.
2. `{}` is an object (labeled drawer of key/value pairs); `[]` is an array (ordered list of items).
3. `https://api.github.com/users/torvalds`
4. Not authenticated — you're missing a valid key or permission (Lesson 2 territory).
5. `?` starts the query parameters; `&` separates multiple `key=value` pairs.
</details>

---

## 9. Homework & what's next

**This week's homework:** explore one new public API on your own — try `https://pokeapi.co` (no key needed). Find the endpoint that returns data for a Pokémon of your choice by name, call it in your browser, and write down three facts you extracted from the JSON (e.g., its height, its types).

**Lesson 2 preview:** API keys and authentication, POST requests, and reading real documentation — plus calling an API from Python or JavaScript so it happens automatically.

**Where to go next in this collection:** [n8n](../n8n/First%20Lesson.md) turns API calls into automations without code; [JavaScript](../JavaScript/First%20Lesson.md) shows how web pages consume APIs; [vector databases](../vector%20databases/First%20Lesson.md) are often just another API away.
