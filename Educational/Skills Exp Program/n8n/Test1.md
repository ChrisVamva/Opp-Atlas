# Test1 — n8n

> **When:** after the [First Lesson](First%20Lesson.md) and its weather-alert homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What two jobs does a workflow's first node do, and what happens without it?

**A2.** In n8n terms, what is an **item**, and what happens to items at a Filter node?

**A3.** What is the difference between the **Schedule Trigger** and the **Manual Trigger / Execute** button — and when do you use each while building?

**A4.** What is the universal node for talking to *any* API?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Pull the `title` field from the previous node: `{{ $json._____ }}`

**B2.** A saved workflow never runs until you toggle it _____.

**B3.** While building, test immediately with the _____ button instead of waiting for the schedule.

**B4.** Data flows through nodes left to _____ along the arrows.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Your local n8n (`localhost:5678`) or n8n.cloud.*

Rebuild the lesson's RSS digester, then extend it:

1. **Schedule Trigger** (daily) → **RSS Read** (`https://hnrss.org/frontpage`).
2. Execute once and record how many items came out.
3. Add a **Filter**: keep only items whose `title` contains a keyword of your choice (case-insensitive). Record how many survived.
4. Add an **Edit Fields (Set)** node keeping only `title` and `link`.
5. Toggle the workflow **Active**.

**Extension (3 pts):** swap the RSS node for an **HTTP Request** node calling `https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true`, and explain in one sentence what the HTTP Request node returned as items (this is the [APIs First Lesson](../APIs/First%20Lesson.md) meeting n8n).

### Rubric
| Points | Standard |
|---|---|
| 12 | Workflow saved and active; filter demonstrably reduces items; Set node configured |
| 5 | You can explain trigger → nodes → items flow and why Execute-while-building matters |
| 3 | Extension completed |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A learner's workflow is saved, perfect — and never runs. The toggle in the top-right is gray.

**D2.** A learner connects the RSS node's output arrow *into* the Schedule Trigger "to send data to it."

**D3.** *(Bonus scenario, not scored separately)*: a Filter for `title` contains `AI` passes zero items even though posts about AI are visibly in the feed — why might case be the culprit?

---

## Part E — Apply & extend (6 pts)

Design (on paper, no build) a morning-digest robot: **Schedule → HTTP Request (weather) → Filter → notification**. In **4–6 sentences**: what triggers it, what the filter condition would be (e.g., temperature below N), what data the final node receives, and why you'd test with **Execute** before activating.

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

**A1.** The trigger starts the run and defines "when"; without a trigger (or manual execution) the workflow never fires. · **A2.** One JSON record flowing between nodes; a Filter lets matching items through and drops the rest (downstream nodes then run once per surviving item). · **A3.** Schedule fires on a clock ("daily at 9:00"); Manual/Execute runs now for testing — use Execute while building, Schedule (or webhooks) in production. · **A4.** The HTTP Request node.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** `title` · **B2.** Active · **B3.** Execute workflow · **B4.** right
</details>

<details><summary><strong>Part C — grading notes</strong></summary>

Graded on the loop: build → Execute → *read the output* (item counts before/after the Filter prove the filter works). The Set node keeping `title`/`link` mirrors the lesson's Step 4. Activation (Step 5) is worth attention — it's the most-forgotten step in real life. Extension: HTTP Request returns the JSON as item(s) — the weather object becomes item data instead of RSS posts.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: not activated — saved ≠ running; the Active toggle is off. Fix: toggle Active. · **D2.** Bug: data flows left→right; the trigger is always the *first* node and its arrow points into the next node, never backwards. Fix: Trigger → RSS. · **D3.** (bonus) The filter is case-sensitive: `AI` ≠ `ai` in titles like "OpenAI ships..." — set the condition to case-insensitive or test with a broader keyword.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

Schedule Trigger (daily morning); HTTP Request with city coordinates + `current_weather=true`; Filter condition like `current_weather.temperature < 5` (or above a threshold); the notification node receives the surviving item (the weather data + chosen message); testing with Execute first because a wrong filter shouldn't wait for tomorrow 9:00 to be discovered — activate only once proven.
</details>
