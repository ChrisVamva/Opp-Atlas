import dspy


class TaskPlanner(dspy.Signature):
    """
    You are a senior software architect planning a development task.
    Given the task and current codebase, produce a concrete execution plan.
    Output `steps` as a valid JSON array of strings — one atomic action per step.
    Output `files_to_touch` as a valid JSON array of relative file paths.
    Be specific. Do not be vague. Prefer small, verifiable steps over large ones.
    """
    task: str = dspy.InputField(desc="The development task to complete")
    codebase_summary: str = dspy.InputField(desc="Project structure and key file contents")

    plan: str = dspy.OutputField(desc="High-level approach and architecture decisions")
    steps: str = dspy.OutputField(desc='Ordered atomic steps as JSON array e.g. ["Read requirements.txt", "Create src/auth.py"]')
    files_to_touch: str = dspy.OutputField(desc='Files to create or modify as JSON array e.g. ["src/auth.py", "requirements.txt"]')
    risks: str = dspy.OutputField(desc="Top 3 risks and how to mitigate each")


class StepDecider(dspy.Signature):
    """
    You are a coding agent deciding exactly which tool to call for a given step.
    Study the step, the file context, and any previous errors carefully.
    Output tool_args as a VALID JSON object — no trailing commas, no comments.

    Available tools and their required args:
    - read_file:      {"path": "relative/path"}
    - write_file:     {"path": "relative/path", "content": "full file content as string"}
    - patch_file:     {"path": "relative/path", "old_content": "exact text to replace", "new_content": "replacement"}
    - append_file:    {"path": "relative/path", "content": "text to append"}
    - run_command:    {"command": "shell command string"}
    - search_code:    {"pattern": "text to search for", "file_extension": ".py"}
    - list_directory: {"path": "relative/path"}
    """
    current_step: str = dspy.InputField(desc="The specific step to execute right now")
    file_context: str = dspy.InputField(desc="Current contents of relevant files")
    completed_steps: str = dspy.InputField(desc="JSON list of already completed steps")
    last_error: str = dspy.InputField(desc="Error from last attempt — empty string if first try")
    project_root: str = dspy.InputField(desc="Absolute path to the project root directory")

    reasoning: str = dspy.OutputField(desc="Step-by-step reasoning for tool choice and args")
    tool_name: str = dspy.OutputField(desc="Exact tool name — must match available tools list")
    tool_args: str = dspy.OutputField(desc="Valid JSON object of arguments for the chosen tool")


class Verifier(dspy.Signature):
    """
    Verify whether a step completed successfully based on the tool result.
    Be strict — only output success=true if the result clearly confirms the step is done.
    An ERROR message in the result means success=false.
    A returncode != 0 in run_command means success=false.
    """
    step: str = dspy.InputField(desc="What was supposed to happen")
    tool_used: str = dspy.InputField(desc="Which tool was called")
    tool_result: str = dspy.InputField(desc="Raw result returned by the tool")

    success: str = dspy.OutputField(desc="true or false")
    issue: str = dspy.OutputField(desc="Specific problem if failed — empty string if success")
    suggestion: str = dspy.OutputField(desc="Concrete fix if failed — empty string if success")
