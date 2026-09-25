# Browser Use UI Prompts for Memory_S_Chip Research

Suggested prompts for Browser Use UI to advance research across the core domains of the Memory_S_Chip system.

---

## 01 Agent Design & Architecture

**Explore Multi-Agent Frameworks**
```
Search for current multi-agent orchestration frameworks (2024-2025). Focus on:
- Supervisor-worker pattern implementations
- Spec-driven or contract-first execution models
- Agent memory and continuity mechanisms
- Comparison of LangGraph, AutoGen, CrewAI, and emerging alternatives

Extract: architectural patterns, not vendor marketing.
```

**Memory-Aware Agent Implementations**
```
Find working examples of agents that maintain session-to-session memory.
Look for:
- Structured memory storage approaches (not just context window stuffing)
- Preference preservation across interactions
- Failure/success pattern tracking
- Continuity mechanisms in open-source projects

Focus on implementations, not theoretical proposals.
```

**Planner-Executor-Verifier Patterns**
```
Search for documented implementations of separated planning and execution roles in agent systems.
Find:
- How the handoff between planner and executor is structured
- Verification mechanisms that don't just repeat the planner's work
- Code examples or architectural documentation

Extract the structural patterns, not surface descriptions.
```

---

## 02 Routing and Observability

**Dynamic Model Routing Systems**
```
Research current approaches to routing requests between different models based on task characteristics.
Find:
- Cost-aware routing logic
- Capability-based model selection
- Fallback and resilience patterns
- Open-source routing layers or brokers

Look for implementation details, not just "we use multiple models" claims.
```

**Agent Observability and Tracing**
```
Search for agent-specific observability tools and patterns (2024-2025).
Focus on:
- Decision tracing in multi-step agents
- Telemetry that captures planning vs execution phases
- Evaluation frameworks for agent output quality
- Tools like Langfuse, LangSmith, AgentOps, or alternatives

Extract: what actually gets traced and how it enables improvement.
```

**Token Efficiency Strategies**
```
Find documented approaches to token-efficient agent operation.
Look for:
- Prompt compression techniques that preserve meaning
- Context pruning strategies
- Tiered model usage (strong model plans, weak model executes)
- Real cost/performance tradeoff analyses

Focus on measurable patterns, not vague "optimize your prompts" advice.
```

---

## 03 Semantic Synthesis Methods

**Structured Reading and Extraction Systems**
```
Search for tools or methods that enforce structured extraction from reading material.
Find:
- Fixed-field extraction (concept, tension, link, seed)
- Reading workflows that force synthesis over accumulation
- Knowledge graph construction from sources
- Zettelkasten or similar methods in digital tooling

Extract: the structural discipline, not the note-taking app features.
```

**Roundtable and Adversarial Reasoning Implementations**
```
Find working examples of multi-perspective or adversarial reasoning in AI systems.
Look for:
- Debate-based fact-checking systems
- Red-teaming implementations in reasoning chains
- Multi-agent consensus mechanisms
- Structured disagreement protocols

Focus on the architecture of controlled disagreement.
```

**Symbolic Compression Techniques**
```
Research methods for compressing complex ideas into reusable symbolic form.
Find:
- Structured shorthand systems (not private ad-hoc abbreviations)
- XML or tag-based extraction patterns in LLM workflows
- Knowledge representation formats that survive compression
- Examples from technical documentation or academic practice

Extract: compression that preserves operability, not just density.
```

---

## 04 Memory Systems Architecture

**Short-Term vs Long-Term Memory in AI Systems**
```
Search for architectures that distinguish between working memory and archive/storage.
Find:
- Episodic memory implementations in agents
- Memory tiering approaches
- Selective recall mechanisms
- Forgetting/expiration strategies (as a feature, not a bug)

Look for system designs that mirror human memory layering.
```

**Obsidian and Personal Knowledge Base Patterns**
```
Research advanced Obsidian workflows for knowledge synthesis (not just storage).
Focus on:
- evergreen note methodologies
- MOC (Map of Content) patterns for orientation
- Periodic review and compression workflows
- Integration with agent or AI-assisted tooling

Extract: the organizational logic, not plugin recommendations.
```

**Memory-Archive Distinctions in Practice**
```
Find systems or methodologies that maintain a clear boundary between:
- Near-surface, immediately available context
- Deep storage that requires retrieval effort
- Distinctions between priming, organizing, and storing

Look for implementation patterns in complex knowledge workflows.
```

---

## 05 Tools and Implementation Landscape

**Current Agent Development Platforms**
```
Survey the 2024-2025 landscape of agent development tools.
Map:
- What each platform actually abstracts (and what it doesn't)
- Where architectural control is preserved vs surrendered
- Integration points with memory, routing, and observability systems
- Lock-in risks and migration paths

Extract: the structural capabilities, not feature checklists.
```

**Integration Patterns: Memory + Agents + Publishing**
```
Search for systems that connect research, agentic processing, and publication.
Find:
- Research-to-writing pipelines with agent assistance
- Memory systems that feed into creative workflows
- Publishing workflows that preserve synthesis quality
- Examples in academic, fiction, or technical writing contexts

Focus on the handoffs between research, processing, and output.
```

**Spec-Driven Development Tools**
```
Find tools or methodologies that enforce contract-first execution.
Look for:
- Interface definition as the primary artifact
- Execution bounded by explicit contracts
- Verification against specification (not just output quality)
- Applications in code generation, content creation, or agent workflows

Extract: the structural discipline, not the syntax of spec formats.
```

---

## 06 Synthesis and Research Method

**Analogy and Cross-Domain Mapping**
```
Search for methods that systematically find structural isomorphisms across domains.
Find:
- Analogical reasoning frameworks
- Domain translation methodologies
- Pattern matching across unrelated fields
- Applications in creative or philosophical work

Focus on the method, not the output.
```

**Compression Without Loss**
```
Research methods for preserving meaning under aggressive compression.
Look for:
- Progressive summarization techniques
- Lossy compression that preserves decision-relevant distinctions
- Shorthand systems that remain explainable
- Examples from technical writing, coding, or academic practice

Extract: the compression logic, not just "be concise" advice.
```

---

## Execution Reminders

**For Each Browse Session:**

1. **Start with the structural question** — What pattern am I looking for?
2. **Extract durable patterns** — Not vendor names or version numbers
3. **Preserve distinctions that change action** — Not generic summaries
4. **Maintain compression discipline** — Can this be understood quickly?
5. **Connect back to the system** — Does this strengthen agent capability, memory structure, or strategic execution?

---

*These prompts are aligned with the Memory_S_Chip philosophy: archive stores, memory organizes, short memory primes.*
