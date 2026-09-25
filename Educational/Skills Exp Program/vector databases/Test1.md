# Test1 — Vector Databases

> **When:** after the [First Lesson](First%20Lesson.md) and its paper-database homework · **Time cap: 35 minutes** · **Total: 50 points**
> Closed book for Parts A, B, D, E. Part C may use the lesson's cheat sheet only.
> Bands: **45–50** excellent · **35–44** solid pass, review misses · **25–34** re-read flagged lesson sections · **<25** redo the First Lesson hands-on.

---

## Part A — Concept check (8 pts · 2 each)

**A1.** What is an embedding, in one sentence a friend would understand?

**A2.** Why did the query *"how do I make soup tasty?"* match *"The chef seasoned the soup with salt"* despite sharing almost no words?

**A3.** What are chunks, and what breaks if you embed a whole 100-page PDF as one point?

**A4.** What does RAG stand for, and what are its two steps?

---

## Part B — Fill the gaps (8 pts · 2 each)

**B1.** Search = "which stored points are the nearest _____ to my question's point?"

**B2.** The standard "how close are these two points" score: _____ similarity.

**B3.** How many neighbors to return: top-_____

**B4.** Before similarity search, the user's question must be embedded by the _____ model that made the stored points.

---

## Part C — Hands-on practical (20 pts)

*Use the lesson's cheat sheet only. Paper + a free embedding playground (e.g., Cohere Playground → Embed).*

1. Take **6 paragraphs** from any article (number them 1–6). This is your mini-database.
2. Write **two queries** about the article's content: one that shares keywords with a paragraph, one that shares *none* but means the same thing.
3. Draw (or describe) the map: which paragraphs cluster, where the two queries land, and the predicted top-2 matches for each query.
4. Embed the paragraphs + queries in the playground; record the top-2 matches per query by similarity score.
5. Compare predictions vs. tool results. Record one place your intuition and the model **disagreed**, and why that's interesting.

**Extension (3 pts):** write the pipeline shape from memory — for "chat with your PDF," name all four stages between documents and matches, plus what the AI receives.

### Rubric
| Points | Standard |
|---|---|
| 12 | Both query types built; predictions vs. tool results recorded; the disagreement analyzed |
| 5 | You can explain why the no-shared-keywords query still matched (meaning-map reasoning) |
| 3 | Extension: chunk → embed → store → search + "AI receives the matches as context" |

---

## Part D — Diagnose the mistake (8 pts · bug 2 + fix 2 each)

**D1.** A team embeds each PDF as one giant vector, and "what does section 4 say about refunds?" retrieves the *wrong* documents.

**D2.** A developer embeds stored documents with model A (OpenAI) but the user's question with model B (a local model) — and search returns nonsense.

**D3.** *(Bonus scenario, not scored separately)*: a user complains semantic search "missed" the one paragraph containing the exact ID they searched. Why is that expected behavior — and what's the standard fix?

---

## Part E — Apply & extend (6 pts)

Design (on paper) a "search my recipe notes" tool. In **4–6 sentences**: what gets chunked and embedded, what happens when the user types a craving ("something warm for a rainy evening"), why it beats keyword search for this case, and one failure mode you'd warn the user about.

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

**A1.** A list of numbers from a model so that texts with similar meanings land close together on a "map of meaning." · **A2.** Their embeddings are close on the map — same *meaning* (making soup taste better), despite almost no shared words. · **A3.** Paragraph-sized pieces embedded separately so a query matches the specific passage; a whole-PDF point matches roughly ("the document mentions refunds somewhere") instead of precisely (the one section). · **A4.** Retrieval-Augmented Generation: (1) retrieve the most similar chunks, (2) hand them to a generative AI as context to write the answer.
</details>

<details><summary><strong>Part B</strong></summary>

**B1.** neighbors · **B2.** cosine · **B3.** k (e.g., top-5) · **B4.** same
</details>

<details><summary><strong>Part C — grading notes</strong></summary>

The paired-query design (shared keywords vs. shared meaning only) is the graded heart: the second query exists to *prove* semantic matching. Grading looks for honest recording of disagreements with the model — that's the learning moment, not a failure. Extension: chunk → embed → store → search; the AI receives the top-k matches as context, not the whole database.
</details>

<details><summary><strong>Part D</strong></summary>

**D1.** Bug: whole-PDF point = coarse matching; matches "somewhere in this doc" instead of the section. Fix: chunk (paragraph-sized pieces) → embed per chunk. · **D2.** Bug: different models = different maps; points from model A can't be compared with points from model B. Fix: same model for everything on one system. · **D3.** (bonus) Semantic search is "closest meaning," not exact-word matching — an exact ID is a keyword problem. Fix: hybrid search (vector + keyword) for exact-identifier queries.
</details>

<details><summary><strong>Part E — what a strong answer includes</strong></summary>

Chunk recipes (per recipe or per paragraph) → embed → store; the craving gets embedded by the same model and the nearest recipe chunks are returned; beats keyword search because "warm/rainy" matches *stew/soup/braise* with zero shared words; warned failure mode: exact matching needs (e.g., "recipe #42" or an unusual ingredient name) may not be the nearest point — pair with keyword search.
</details>
