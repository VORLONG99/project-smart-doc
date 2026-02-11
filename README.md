# Project Smart Documentation Skill

**Project Smart Documentation** is an intelligent assistant designed to automate the maintenance of project documentation. It goes beyond simple file generation by deeply analyzing code to uncover "hidden knowledge," identifying technical debt, and ensuring critical project information remains up-to-date.

## Core Capabilities

This skill provides three main functions to keep your project documentation healthy and accurate.

### 1. Deep Project Initialization & Analysis

Automatically scans your entire codebase to generate a comprehensive `project_overview.md`.

- **Trigger**: First use or explicit request (e.g., "Initialize docs", "Analyze project").
- **What it does**:
  - **Architecture Detection**: Identifies project type (React, Node.js, etc.) and entry points.
  - **Dependency Analysis**: Lists core tech stack and versions from package files.
  - **Environment Check**: Summarizes configuration needs from `.env` and config files.
  - **Hidden Knowledge Mining**: Aggregates `TODO`, `FIXME`, `HACK`, and `NOTE` comments to expose technical debt and complex logic.

### 2. Smart Capture & Dynamic Update

Actively listens to your conversations to capture and record critical business logic and caveats.

- **Trigger**:
  - **Explicit**: Keywords like "pay attention to", "note that", "crucial point".
  - **Implicit**: When you explain complex logic or correct the AI's understanding.
- **What it does**:
  - Updates `doc/attention_points.md` with new findings.
  - **Strict Separation**: Ensures business logic is kept separate from commit logs.
  - **Contextual**: Links notes to specific code modules where applicable.

### 3. Smart Commit Overview

Generates structured summaries for significant code changes.

- **Trigger**: Large commits (>100 lines or >3 files) or explicit request.
- **What it does**:
  - Updates `doc/commit_history.md`.
  - **Structured Log**: categorization by type (Feature/Fix/Refactor).
  - **Impact Analysis**: Lists affected modules and potential risks.

### 4. Deep Logic & Algorithm Analysis

Digs deep into the "why" and "how" of complex implementations.

- **Trigger**: Requesting analysis of core logic, or when AI encounters unconventional patterns (monkey patches, complex regex, custom middleware).
- **What it does**:
  - Creates `doc/core_logic.md`.
  - Explains **rationale**, **edge cases**, and **side effects**.
  - Visualizes implementation mechanisms (via text descriptions/pseudocode).

### 5. Migration & Refactoring Assistant

Guides you through large-scale changes and keeps track of the plan.

- **Trigger**: Keywords like "migration", "refactoring", "upgrade", "switching DB".
- **What it does**:
  - Creates `doc/migration_guide.md` or `doc/refactoring_notes.md`.
  - **Gap Analysis**: Compares current vs. target state.
  - **Risk Assessment**: Identifies compatibility issues and data migration risks.
  - **Action Plan**: Generates step-by-step execution guides.

### 6. Self-Evolution & Upgrade

Capable of modifying its own rules to better suit your workflow.

- **Trigger**: Direct requests like "Upgrade this skill", "Add a rule to docs", or repeated corrections of its behavior.
- **What it does**:
  - Analyzes your request to understand what behavior needs changing.
  - **Self-Modifies**: Edits its own `SKILL.md` file in `.trae/skills/` to permanently adopt the new rule.
  - **Logs**: Records the upgrade in the skill definition for transparency.

## Documentation Structure

The skill maintains a `doc/` directory with a clean, separated structure:

| File                  | Purpose                                                                             |
| --------------------- | ----------------------------------------------------------------------------------- |
| `project_overview.md` | Macro-level project view, architecture, tech stack, and **technical debt summary**. |
| `attention_points.md` | **Dynamic** business logic, pitfalls, and special configuration notes.              |
| `commit_history.md`   | Structured log of major code changes and version iterations.                        |
| `core_logic.md`       | Deep dive into complex algorithms, hacks, and unconventional implementations.       |
| `migration_guide.md`  | Roadmap and checklist for large-scale refactoring or technology migration.          |

## Installation

1. Copy the `project-smart-doc` folder to your project's `.trae/skills/` directory.
2. The skill will automatically activate based on the triggers described above.

## How to View Evolution Logs

You can check the self-evolution history of this skill by viewing the bottom of the `SKILL.md` file.

```bash
# View the evolution log
tail -n 20 .trae/skills/project-smart-doc/SKILL.md
```

Or simply ask me: "Show me the skill evolution log."
