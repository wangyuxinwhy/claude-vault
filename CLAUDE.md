## Core Principle

- **Think twice, code once**: Communicate with the user first, clarify intent and scope, get explicit authorization before taking action.
- Do not assume user intent—when in doubt, ask instead of guessing and executing.
- Before any side-effecting operation (installing dependencies, writing files, running scripts), explain the plan and get confirmation.
- Ask for context when uncertain — good questions help the user think, not just help you execute.
- When presenting options, always give your recommendation with reasoning. Have a point of view.

## Code Style

### Comments

- Let the code speak for itself: prefer clear naming, small functions, and type hints over inline comments.
- Delete outdated comments—stale comments are worse than no comments.
- Add comments only when necessary to explain **why** or **how** (intent, constraints, trade-offs), NOT **what** the code does.
- **Do comment** when the intent is non-obvious: business rules, performance trade-offs, compatibility quirks, security assumptions, temporary workarounds.

### Docstrings

- **Required** for all public modules, classes, functions, and methods.
- Follow Google Python Style Guide for docstring format.
- Use type hints for types; docstrings focus on **purpose**, **semantics**, and **exceptions**.
- For internal/private helpers, docstrings are optional—only add when behavior is non-trivial.

## Python

- Always use `uv` for Python projects: `uv run`, `uv add`, `uv sync`, `uv venv`.
- Never use bare `python`/`python3` or `pip`/`pip3` commands.

## Git

### Commit Message

- Use imperative mood: "Add feature" not "Added feature".
- Be specific: describe what changed and why, not vague "Update code".
- Follow conventional format: `<type>: <subject>` (feat, fix, refactor, docs, style, chore).

### Commit Granularity

- One commit, one logical change—single responsibility principle.
- Each commit should be independently revertable.
- Group related changes together; separate unrelated changes.

## Long-Running Tasks

### Progress Output

- Always output progress at key checkpoints—never leave users staring at a blank screen.
- Use `print(..., flush=True)` or equivalent to ensure real-time output.
- For batch operations, print: current item, total count, and brief status (e.g., `[3/10] Processing foo... done`).
- For multi-stage tasks, announce each stage start/end (e.g., `=== Stage 2: Testing ===`).
- If a single operation takes >10s, consider a simple indicator (dots, spinner, or periodic status).

### Parallelization

- Prefer parallel execution for independent tasks—don't run sequentially what can run concurrently.
- Use `concurrent.futures.ThreadPoolExecutor` or `asyncio` for I/O-bound tasks (API calls, file ops).
- Respect rate limits: add concurrency cap (e.g., `max_workers=5`) to avoid overwhelming external services.
- For Claude Code itself: invoke multiple tools in a single message when they are independent; use multiple `Task` sub-agents in parallel for complex work.
- Balance: parallelism speeds things up, but excessive concurrency can cause throttling or errors.
