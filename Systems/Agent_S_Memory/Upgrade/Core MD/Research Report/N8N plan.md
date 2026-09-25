# Summary of N8N Notes

## Overall theme
These notes document the design and refinement of an **n8n-based daily intelligence workflow** that gathers research, filters it through a strong editorial lens, and saves the result into Obsidian. The broader goal is not automation for its own sake, but building a **practical research pipeline** that produces notes worth keeping: decisions, reusable insights, and operational next steps.

## Core workflow vision
The central system described across the notes is an **Afternoon Intelligence Pipeline**:

1. **n8n** acts as the scheduler and orchestrator
2. **Browser Use** gathers research from targeted sources
3. **An AI summarization/personalization layer** reshapes the findings into something useful
4. **Obsidian** becomes the final knowledge destination

The intended result is a daily note, saved automatically into the vault, containing only high-signal material.

## Main architectural conclusion
The workflow evolved from an initial idea of:

`Schedule → Browser Use → OpenClaw → Obsidian`

toward a more practical and simpler implementation:

`Schedule → Research sources → Format → Mistral summarizer / n8n AI Agent → Obsidian`

The key insight is that **OpenClaw may not be the right bottleneck for this pipeline**. While it may still be useful elsewhere, the notes conclude that n8n’s own AI layer or a direct Mistral step is cleaner, easier to maintain, and requires less reverse-engineering.

## Important system pieces

### 1. Browser Use inside n8n
- The workflow relies on the `n8n-nodes-browser-use` community package
- Browser Use is treated as the **researcher** in the system
- It is expected to collect structured findings on topics like:
  - AI agent frameworks and releases
  - browser automation and scraping developments
  - multi-agent orchestration patterns
  - model routing changes
  - worthwhile new tools in the agentic ecosystem

### 2. Obsidian as final storage
- Obsidian is the long-term destination for the output
- The **Local REST API** plugin is required
- The note is written to a dedicated path such as:
  - `/N8N/Daily Intelligence/YYYY-MM-DD.md`
- This matches the note philosophy of keeping research structured, dated, and easy to revisit

### 3. AI processing layer
Two options appear in the notes:
- **OpenClaw** as a personalization layer
- **Mistral or n8n AI Agent node** as a simpler summarizer/personalizer

The later notes lean toward the second option as more realistic and less fragile.

## The note philosophy behind the system
One of the strongest threads in these notes is that the pipeline is shaped by a strict editorial rule:

> Research should end in a decision, a reusable note, or an operational next step. If it produces none of these, it should not survive.

That principle drives the summarizer prompt and determines what gets saved. The goal is not a generic news digest, but a **survival-filtered intelligence brief**.

The expected note sections include things like:
- **Signal**
- **Tools Worth Watching**
- **What to Ignore**
- **Next Steps**

## Practical setup sequence that emerges
The notes repeatedly refine the correct setup order. The clearest sequence is:

1. Install **Browser Use** community node in n8n
2. Install **Obsidian Local REST API** plugin and copy its API key
3. Build/import the n8n workflow JSON
4. Run a manual test
5. Verify the generated note appears in Obsidian
6. Activate the daily schedule

This ordering matters because the workflow cannot save notes without the Obsidian API already configured.

## Technical details captured in the notes
Several operational details are established:

- **Obsidian Local REST API** default port: `27123`
- **OpenClaw Gateway** identified at: `http://localhost:18789`
- **OpenClaw Bridge** identified at: `http://localhost:18790`
- Browser Use is intended to run as a local/self-hosted component
- n8n is running in Docker in at least part of this setup

There is also a real workflow file mentioned:
- `daily_intelligence_workflow.json`

## What was learned about OpenClaw
A notable correction appears in the notes:
- OpenClaw was initially treated as if it were a straightforward REST endpoint for n8n
- After further investigation, that assumption became less certain
- The more honest conclusion is that OpenClaw is better understood as a messaging gateway and may not be the best integration point here

This is an important pattern: the notes favor **honest reassessment over forcing architecture**.

## Implementation friction and constraints
The notes also record practical issues:

### Docker / n8n setup friction
- Community nodes may require `N8N_COMMUNITY_PACKAGES_ENABLED=true`
- If GUI install is unavailable, installation may need to happen inside the container

### Reddit scraping friction
- Reddit returned **403 Forbidden** for automated requests from the n8n container
- The practical fix was to disable the Reddit node temporarily
- Hacker News and GitHub were sufficient to get the rest of the pipeline working
- If Reddit is needed later, the official Reddit node with OAuth is the proper path

This reflects a larger design principle in the notes: **get the pipeline working first, then improve edge sources later**.

## User/workflow identity inferred from the notes
The notes repeatedly describe a builder focused on:
- agentic systems
- tool evaluation with verdicts, not hype
- model routing
- strategic filtering
- research compression into reusable knowledge

The N8N workflow is therefore not just automation infrastructure. It is a **daily intelligence engine** designed to feed a broader thinking and creation system.

## Strategic takeaways
Across all the notes, the strongest conclusions are:

- **n8n is the orchestrator**, not the intelligence itself
- **Browser Use is the research collector**
- **Obsidian is the memory layer**
- **The summarizer must enforce a survival filter**
- **Simple, reliable integration beats elegant but fragile architecture**
- **Testing the whole path end-to-end matters more than theoretical completeness**

## Practical action items distilled from the folder
- [ ] Install or verify `n8n-nodes-browser-use`
- [ ] Enable community packages in Docker if needed
- [ ] Install and configure Obsidian Local REST API
- [ ] Import or rebuild `daily_intelligence_workflow.json`
- [ ] Test the workflow manually before scheduling it
- [ ] Confirm note output path in the active vault
- [ ] Keep Reddit disabled unless proper OAuth is added
- [ ] Decide whether OpenClaw should stay out of this pipeline entirely
- [ ] Refine the summarizer prompt to better reflect the survival-test philosophy
- [ ] Let the workflow produce daily notes consistently before expanding scope

## One-paragraph synthesis
These notes show the formation of a grounded, useful N8N system: a scheduled research pipeline that collects signals, filters them through a hard editorial standard, and saves the result into Obsidian as a dated intelligence note. The biggest architectural lesson is that the workflow becomes stronger as it becomes simpler: Browser Use for collection, Mistral or n8n AI for summarization, and Obsidian for storage. The whole design is driven by a clear philosophy — if a piece of research does not lead to a decision, a reusable insight, or a next step, it should not survive.
