# Summary of TO DO LIST Notes

## Overall theme
These notes describe a shift from scattered experimentation with many AI tools toward a more disciplined, grounded, and integrated workflow. The core pattern is clear: tools are valuable when they increase clarity, continuity, and execution speed; they become harmful when they add complexity, hallucination risk, or uncontrolled autonomy.

## Main ideas across the notes

### 1. The real bottleneck is orchestration, not lack of tools
You already have access to many capable systems: coding agents, reasoning models, research tools, and an Obsidian knowledge base. The problem is not scarcity of capability, but lack of a handoff protocol between brainstorming, planning, implementation, and review.

### 2. AI agents need strict guardrails
The notes repeatedly stress that current agentic AI is powerful but unsafe by default. Common failure modes include infinite loops, hallucinated paths/configs, reckless tool use, and destructive actions without enough confirmation. Strong limits, sandboxing, checkpoints, confirmation steps, and cautious model selection are treated as essential.

### 3. Grounding matters more than raw model intelligence
For technical/configuration work, the key distinction is between:
- generating plausible answers
- verifying against real files, docs, and current environment

The recommended direction is to force grounding before writing configs or making technical decisions.

### 4. Obsidian should become the memory backbone
A major insight is that your Obsidian vault can solve the continuity problem. Instead of relying on model memory, you should maintain structured context notes such as `PROJECT_CONTEXT.md`, planning files, decision logs, and summaries. This makes sessions portable across tools and reduces hallucination.

### 5. Separate thinking from implementation
One of the strongest patterns in the notes is that brainstorming and implementation should not happen in the same uncontrolled loop. Strategy should happen in one layer, verified planning in another, file-writing in another, and review in another. This separation reduces costly confusion.

### 6. Build only focused, high-ROI automations first
Because time is tightening, the recommendation is not to automate everything. Start with predictable, repetitive, isolated tasks. The Orange Tomato visual asset pipeline is identified as the best first automation candidate.

## Tool and workflow conclusions

### Tools that were seen as valuable
- Claude Code + Gemma 4 31B in Zed
- OpenClaw / LUX
- OpenRouter
- Exa + Firecrawl MCPs
- KiloCode
- Windsurf / Cascade
- Opencode
- Aider
- Obsidian as the memory layer
- Browser-grounded research workflows

### Tools or setups that were rejected or treated cautiously
- OpenHands (functional but not compelling)
- ACP bridge / acpx / Codex integration due to instability and hallucinated success
- Cursor free plan limitations
- Devin reliability concerns
- Broad autonomous agent permissions without guardrails
- Direct local terminal access for agents

## Strategic direction that emerges
The direction is toward a smaller, sharper stack with clearer role boundaries:

1. **Thinking layer**: idea development, reflection, exploration
2. **Planning layer**: grounded research, architectural decisions, documentation
3. **Implementation layer**: tools that can see the real filesystem and edit actual files
4. **Review layer**: git-aware inspection and manual validation

This direction favors coherence over novelty.

## Product and creative vision
A significant thread running through the notes is the Orange Tomato vision:
- a personal blog/site with a unified voice and visual identity
- hand-drawn mascot-based artwork
- AI-supported art direction
- visual breakers, score sheets, schematics, and editorial structure
- a long-term goal of combining strategic reasoning, creative direction, and implementation into one coherent system

There is also a broader repo/product consolidation vision: multiple small repos appear to be fragments of one larger idea and should likely be merged into a more unified structure.

## Pain points identified

### Operational pain
- too many tools without clear coordination
- time lost to setup, integration, and debugging
- context switching across multiple active projects
- wasted effort when exploratory AI guesses are applied directly to configs

### Technical pain
- hallucinated file paths and model names
- outdated or fabricated config guidance
- Windows friction in open-source agent workflows
- model/tool interoperability issues
- insufficient safety on autonomous actions

### Human pain
- frustration from losing context
- fatigue from repeated re-explanation
- anger from agents acting beyond intended permission boundaries
- overwhelm from having more resources than can be effectively orchestrated

## Recommended operating principles
- Use AI for decisions first, file changes second
- Require verification before generating technical values
- Keep a structured project context document for every serious project
- Use filesystem-aware tools for implementation
- Keep destructive operations behind human confirmation
- Start automating repetitive chores, not complex R&D workflows
- Prefer fewer integrated tools over many loosely connected ones
- Preserve summaries and daily research compressions as reusable assets

## Practical action items distilled from all notes
- [ ] Merge the related repos into one larger coherent repo structure
- [ ] Create and maintain project context files in Obsidian for active projects
- [ ] Formalize a handoff workflow between thinking, planning, implementation, and review
- [ ] Add hard safety guardrails for all agentic workflows
- [ ] Avoid giving agents unsandboxed terminal/file-system power
- [ ] Build the first automation around the Orange Tomato art pipeline
- [ ] Define the Orange Tomato site architecture, voice, art direction, and visual system
- [ ] Mark article structure points for tables, Excalidraw diagrams, and visual breaks
- [ ] Set up a more deliberate conversational workflow with LUX/OpenClaw
- [ ] Continue evaluating which tools genuinely reduce complexity
- [ ] Monitor actual limits, costs, and reliability of each resource
- [ ] Preserve daily research outputs as compressed summaries for later article production

## One-paragraph synthesis
The notes show a maturing systems view: the challenge is no longer discovering powerful AI tools, but designing a workflow that forces clarity, grounding, safety, and continuity. The strongest emerging architecture combines Obsidian as memory, grounded research for planning, filesystem-aware agents for implementation, and explicit review before changes are applied. The next stage is to simplify the stack, consolidate projects, and build a few highly targeted automations that protect your time while reinforcing the Orange Tomato creative and technical vision.
