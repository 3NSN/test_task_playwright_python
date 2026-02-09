# UI Automation Framework

test task
Contains 3 test cases, and demonstrate POM

## Tech Stack

* **Language:** Python 3.10+
* **Core:** Playwright (Synchronous API)
* **Runner:** Pytest
* **Environment & Dependencies:** uv
* **Orchestration:** tox
* **Linting:** Ruff

## Prerequisites

* Python 3.10 or higher
* Make (optional, for shorthand commands)

## Quick Start

### Option A: Using Makefile (Recommended)

If `make` is installed, use the following commands:

1.  **Initialize Environment**
    Installs `uv`, creates a virtual environment, and installs `tox`.
    ```bash
    make setup
    ```

2.  **Run Tests**
    Executes tests via `tox` in an isolated environment. This includes automatic browser installation.
    ```bash
    make test
    ```
3.  **Run Tests with UI**
    Executes tests via `tox` in an isolated environment. This includes automatic browser installation.
    ```bash
    make test-ui
    ```

4. **Lint Code**
    Checks code style using `ruff`.
    ```bash
    make lint
    ```

### Option B: Manual Execution

If `make` is not available, use `uv` directly:

1.  **Install uv**
    ```bash
    pip install uv
    ```

2.  **Run Tests**
    This command creates the environment and runs the tests using the project's configuration.
    ```bash
    uv run tox -- --headed
    ```
