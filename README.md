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

## Documentation Structure

The skill maintains a `doc/` directory with a clean, separated structure:

| File | Purpose |
|------|---------|
| `project_overview.md` | Macro-level project view, architecture, tech stack, and **technical debt summary**. |
| `attention_points.md` | **Dynamic** business logic, pitfalls, and special configuration notes. |
| `commit_history.md` | Structured log of major code changes and version iterations. |

## Installation

1. Copy the `project-smart-doc` folder to your project's `.trae/skills/` directory.
2. The skill will automatically activate based on the triggers described above.
