# COMP5530MGroupProject
# Mobile Bimanual Robot (MuJoCo)

This project develops and integrates a mobile, bimanual robot in MuJoCo. Work is divided into base mobility, individual arm control, hand grasping, bimanual coordination, and planning.

## Python and environment

Use Python 3.11.

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the demo

```powershell
python examples/demo.py
```

The demo loads the shared robot and scene and starts a headless physics step loop.

## Test

```powershell
pytest
ruff check .
```

Run only fast unit tests with:

```powershell
pytest -m "not slow and not integration"
```

## Repository layout

```
.
├── models/                 # The ONE shared robot model + scenes (no private copies)
│   ├── robot.xml           # Base + 2 Panda arms + hands; everyone loads this
│   └── scenes/             # Shared scene + personal test scenes (include robot.xml)
├── src/
│   ├── common/             # Interfaces, shared data types, stubs others can test against
│   ├── collision/          # Shared configuration-space collision checks
│   ├── mobility/           # Task 1: base control
│   ├── arm/                # Task 2: individual-arm control
│   ├── hand/               # Task 3: hand and grasping
│   ├── bimanual/           # Task 4: bimanual coordination
│   └── planning/           # Task 5: planning
├── tests/
│   ├── unit/               # Fast tests for single functions (run on every push)
│   ├── integration/        # Several tasks together in the shared scene
│   └── fixtures/plans/     # Example LLM plans everyone tests against
├── examples/               # Runnable demos (supervisor meetings, poster videos)
├── docs/
│   ├── architecture.md     # How tasks connect: diagrams + interfaces
│   ├── conventions.md      # Frames, units, timestep, naming
│   └── decisions.md        # Decision log: add each decision at the bottom
├── .github/                # Issue template for Kanban cards (CI workflow added later)
├── requirements.txt        # Pinned versions so everyone's sim behaves the same
└── pyproject.toml          # pytest + ruff settings
```

New to the repo? See the [Repo Guide](../../wiki/Repo-Guide) in the wiki for what each part is for and how to use it.

Before writing code that talks to another task, read [docs/conventions.md](docs/conventions.md) and [docs/architecture.md](docs/architecture.md).

## Team workflow

- Use branch names `taskN/short-description`, or `setup-short-description` for repo, docs and tooling work.
- Commit messages use `taskN: short description`, or `setup: short description` for repo, docs and tooling work.
- Open a pull request for every change; require one approval and passing CI.
- Fix a broken `main` before starting unrelated work.
- Thursday check-ins report done, next, and blockers.
- Meeting minutes, references and AI-usage logs go in the [wiki](../../wiki).
- Scrum Master responsibility rotates; Kavisha holds the first block.