# Documentation Templates

## `doc/project_overview.md`

```markdown
# Project Overview

## 1. Project Summary
- Name:
- Purpose:
- Scope:

## 2. Architecture
- Type: (e.g. monolith / frontend + backend / microservices)
- Entry points:
- Key modules:

## 3. Tech Stack
- Runtime:
- Frameworks:
- Data layer:
- Infra / third-party:

## 4. Environment & Configuration
- Required env vars:
- External dependencies:
- Local setup notes:

## 5. Directory Responsibilities
- `src/`:
- `api/`:
- `scripts/`:

## 6. Marker Summary (TODO/FIXME/HACK/NOTE/XXX/DEPRECATED)
- Total:
- By marker:
- By module:

## 7. Technical Debt & Risks
- [High] ...
- [Medium] ...
- [Low] ...
```

## `doc/attention_points.md`

```markdown
# Attention Points

## [YYYY-MM-DD] <Rule Title>
- Status: New | Updated
- Module: <path or module name>
- Context: <when this matters>
- Rule: <must / must not>
- Bad example: <optional>
- Correct approach: <optional>
```

## `doc/commit_history.md`

```markdown
# Commit History

## [YYYY-MM-DD] <Change Title>
- Type: Feature | Fix | Refactor | Chore
- Summary:
  - <module>: <change>
- Impact:
  - <runtime / api / data / ui>
- Risks:
  - <risk item or None>
- Verification:
  - <tests/checks/manual>
- Files:
  - `<path>`
```

## `doc/core_logic.md`

```markdown
# Core Logic Analysis

## <Module or Algorithm Name>
- Background:
- Rationale:
- Mechanism:
  - Step 1:
  - Step 2:
- Edge cases:
- Side effects:
- Alternatives:
```

## `doc/migration_guide.md`

```markdown
# Migration Guide

## Goal
- Current state:
- Target state:

## Gap Analysis
- Contract/API changes:
- Data model changes:
- Compatibility concerns:

## Execution Plan
1. Preparation
2. Migration steps
3. Rollback plan
4. Validation checklist
```

## `doc/refactoring_notes.md`

```markdown
# Refactoring Notes

## Goal
- Problem:
- Refactor scope:
- Non-goals:

## Plan
1. Baseline and safety checks
2. Incremental refactor steps
3. Behavior parity checks

## Risks & Mitigations
- Risk:
- Mitigation:

## Validation
- Unit tests:
- Integration checks:
- Manual scenarios:
```
