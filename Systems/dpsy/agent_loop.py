import sys
import json
import dspy
import phoenix as px
from openinference.instrumentation.dspy import DSPyInstrumentor
from phoenix.otel import register

from agent_tools import (
    scan_project, format_project_summary,
    read_file, write_file, patch_file, append_file,
    run_command, search_code, list_directory,
)
from agent_modules import TaskPlanner, StepDecider, Verifier

tracer_provider = register(
    project_name="dspy-agent",
    endpoint="http://localhost:6006/v1/traces",
)
DSPyInstrumentor().instrument(tracer_provider=tracer_provider)

lm = dspy.LM("ollama/devstral-2:123b-cloud")
dspy.configure(lm=lm)

planner = dspy.ChainOfThought(TaskPlanner)
decider = dspy.ChainOfThought(StepDecider)
verifier = dspy.ChainOfThought(Verifier)


def make_tools(project_root: str) -> dict:
    return {
        "read_file":      lambda **kw: read_file(project_root=project_root, **kw),
        "write_file":     lambda **kw: write_file(project_root=project_root, **kw),
        "patch_file":     lambda **kw: patch_file(project_root=project_root, **kw),
        "append_file":    lambda **kw: append_file(project_root=project_root, **kw),
        "run_command":    lambda **kw: run_command(cwd=project_root, **kw),
        "search_code":    lambda **kw: search_code(root_dir=project_root, **kw),
        "list_directory": lambda **kw: list_directory(project_root=project_root, **kw),
    }


def get_file_context(files: list, project_root: str, max_chars: int = 6000) -> str:
    parts = []
    total = 0
    for path in files:
        content = read_file(path, project_root=project_root)
        if not content.startswith("ERROR"):
            snippet = f"\n--- {path} ---\n{content[:2500]}"
            if total + len(snippet) > max_chars:
                break
            parts.append(snippet)
            total += len(snippet)
    return "\n".join(parts) if parts else "No existing files yet."


def run_agent(task: str, project_root: str):
    SEP = "=" * 60
    DIV = "-" * 50

    print(f"\n{SEP}")
    print("  DSPy CODING AGENT")
    print(f"  Task:    {task}")
    print(f"  Project: {project_root}")
    print(f"{SEP}\n")

    tools = make_tools(project_root)

    print("📁 Scanning project...")
    scan = scan_project(project_root)
    codebase_summary = format_project_summary(scan)
    print(f"   {scan['total_files']} files found\n")

    print("🧠 Planning...")
    plan_result = planner(task=task, codebase_summary=codebase_summary)

    try:
        steps = json.loads(plan_result.steps)
    except json.JSONDecodeError:
        steps = [s.strip() for s in plan_result.steps.splitlines() if s.strip()]

    try:
        files_to_touch = json.loads(plan_result.files_to_touch)
    except json.JSONDecodeError:
        files_to_touch = []

    print(f"\n📋 Plan:\n   {plan_result.plan}")
    print(f"\n📄 Files: {files_to_touch}")
    print(f"\n⚠️  Risks:\n   {plan_result.risks}")
    print(f"\n🔢 {len(steps)} steps:")
    for i, s in enumerate(steps, 1):
        print(f"   {i:2}. {s}")
    print()

    completed_steps = []
    failed_steps = []

    for i, step in enumerate(steps, 1):
        print(f"{DIV}")
        print(f"⚡ Step {i}/{len(steps)}: {step}")

        last_error = ""
        step_done = False

        for attempt in range(1, 4):
            if attempt > 1:
                print(f"   🔄 Attempt {attempt}/3  |  Last error: {last_error[:120]}")

            file_context = get_file_context(files_to_touch, project_root)

            decision = decider(
                current_step=step,
                file_context=file_context,
                completed_steps=json.dumps(completed_steps),
                last_error=last_error,
                project_root=project_root,
            )

            print(f"   💭 {decision.reasoning[:180].strip()}...")
            print(f"   🔧 {decision.tool_name}  args={decision.tool_args[:120]}")

            try:
                tool_args = json.loads(decision.tool_args)
            except json.JSONDecodeError as e:
                last_error = f"tool_args is not valid JSON: {e} — got: {decision.tool_args[:200]}"
                continue

            if decision.tool_name not in tools:
                last_error = f"Unknown tool '{decision.tool_name}'. Choose from: {list(tools.keys())}"
                continue

            try:
                raw_result = tools[decision.tool_name](**tool_args)
            except TypeError as e:
                last_error = f"Wrong args for {decision.tool_name}: {e}"
                continue
            except Exception as e:
                last_error = f"Tool crashed: {e}"
                continue

            result_str = str(raw_result)
            print(f"   📤 {result_str[:250]}")

            check = verifier(step=step, tool_used=decision.tool_name, tool_result=result_str)

            if check.success.strip().lower() == "true":
                print(f"   ✅ Verified")
                completed_steps.append(step)
                step_done = True
                break
            else:
                last_error = check.issue
                print(f"   ❌ {check.issue}")
                print(f"   💡 {check.suggestion}")

        if not step_done:
            print(f"   ⛔ Gave up after 3 attempts")
            failed_steps.append(step)

    print(f"\n{SEP}")
    print("  DONE")
    print(f"  ✅ {len(completed_steps)}/{len(steps)} steps completed")
    if failed_steps:
        print(f"  ❌ {len(failed_steps)} failed:")
        for s in failed_steps:
            print(f"     • {s}")
    print(f"  📊 Traces → http://localhost:6006")
    print(f"{SEP}\n")

    return {"completed": completed_steps, "failed": failed_steps, "total": len(steps)}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python agent_loop.py <project_root> <task>")
        print()
        print("Examples:")
        print('  python agent_loop.py C:\\Users\\user\\myapp "Add user authentication with JWT"')
        print('  python agent_loop.py . "Refactor database module to use SQLAlchemy"')
        sys.exit(1)

    project_root = sys.argv[1]
    task = " ".join(sys.argv[2:])
    run_agent(task, project_root)
