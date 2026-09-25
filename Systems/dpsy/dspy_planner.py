import dspy
from phoenix.otel import register
from openinference.instrumentation.dspy import DSPyInstrumentor

# ── Phoenix wiring ──────────────────────────────────────────
tracer_provider = register(
    project_name="dspy-planner",
    endpoint="http://localhost:6006/v1/traces"
)
DSPyInstrumentor().instrument(tracer_provider=tracer_provider)

# ── Model ───────────────────────────────────────────────────
lm = dspy.LM(
    model="ollama_chat/devstral-2:123b-cloud",
    api_base="http://localhost:11434",
    api_key="ollama"
)
dspy.configure(lm=lm)

# ── Signature ───────────────────────────────────────────────
class TaskPlanner(dspy.Signature):
    """
    You are a careful software planner.
    Never invent file paths, config values, or dependencies.
    Only reference what is explicitly provided.
    If something is unknown, say UNKNOWN — never guess.
    """
    task    = dspy.InputField(desc="What the developer wants to build or fix")
    context = dspy.InputField(desc="Existing files, configs, or code snippets provided")

    plan    = dspy.OutputField(desc="Step by step plan, numbered")
    files   = dspy.OutputField(desc="Exact files to create or modify. UNKNOWN if not determinable from context")
    risks   = dspy.OutputField(desc="What could go wrong. Be specific, not generic")

planner = dspy.ChainOfThought(TaskPlanner)

# ── Run ─────────────────────────────────────────────────────
result = planner(
    task="Add a save button to the drawing app that saves the canvas as PNG",
    context="Project uses vanilla JavaScript. Main files: index.html, canvas.js, toolbar.js. No backend."
)

print("PLAN:\n",   result.plan)
print("\nFILES:\n", result.files)
print("\nRISKS:\n", result.risks)
