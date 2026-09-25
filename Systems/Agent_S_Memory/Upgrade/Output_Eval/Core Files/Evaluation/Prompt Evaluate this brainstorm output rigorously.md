---
modified: 2026-04-23T00:28:45+03:00
---
Evaluate this brainstorm output rigorously.

You are acting as an expert evaluator, not a collaborator and not a brainstormer.

Task:  
Judge the idea set, reject weak ideas, and identify the strongest survivors.

Scoring criteria:  
Rate each idea from 1 to 5 on:

- Ambition
- Zero-Cost Feasibility
- Market Gap
- Clarity
- Actionability
- Cross-Industry Potential

Hard rejection rules:  
Automatically reject any idea with:

- Market Gap below 4
- Clarity below 4
- Actionability below 4
- Zero-Cost Feasibility below 4 if zero-cost is a requirement for this run

For each idea, output:

- Scores by criterion
- Average score
- Verdict: Survives / Rejected
- Reason in 2-4 sentences

Then do this:

1. List all rejected ideas with the exact failure mode:
    - generic
    - weak gap
    - unclear mechanism
    - false novelty
    - not actionable
    - not truly zero-cost
    - too narrow
    - too incremental
2. From the survivors, produce a ranked Top 3.

For each Top 3 idea, include:

- Why it survived
- What makes it stronger than the others
- Main risk
- Confidence level: Low / Medium / High

3. Choose one final winner.

For the final winner, include:

- Why this is the best candidate now
- What makes it stronger than the #2 idea
- Whether the main strength is market gap, timing, leverage, or originality

4. Final challenge:  
    Name one Top 3 idea that might still be false novelty and explain why.

Output style:

- be blunt
- force a decision
- no diplomatic padding
- no “all of these have promise”

**Secondary Prompt: Prompt Diagnosis**  
Use this when the brainstorm set is weak and you want ChatGPT to evaluate the prompt quality rather than the ideas:

Diagnose why this brainstorm output is weak.

Your job is to identify whether the failure came from:

- the original prompt
- the brainstormer’s interpretation
- weak evaluation criteria upstream
- weak source constraints
- lack of market anchoring
- false ambition without specificity

Output in this structure:

1. Main failure mode
2. Evidence from the output
3. What kind of weakness it produced
4. Minimum prompt change needed
5. Stronger replacement wording for that one section only