# Cursor setup for this project

## Rules (`.cursor/rules/`)

| Rule | When it applies |
|------|-----------------|
| **always.mdc** | Every conversation (project context, env, LangChain stack) |
| **python-notebooks.mdc** | When you have `.py` or `.ipynb` files open |

Add more `.mdc` files here for other file types or conventions. Use `globs` for file-specific rules and `alwaysApply: true` for global rules.

## Account-level agents (all your projects)

To affect **every project** in this Cursor account:

- **Rules**: Add rules under `~/.cursor/rules/` (same `.mdc` format).
- **Skills**: Add skills under `~/.cursor/skills/` (each skill is a folder with a `SKILL.md`). Skills teach the agent specific workflows (e.g. commit messages, code review, PDF handling).

Project rules here take effect only in this repo; account rules apply everywhere.
