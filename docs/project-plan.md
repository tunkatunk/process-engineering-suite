# Project Plan: Process and Safety Engineering Software Suite

## Overview
This project develops a modular software suite for process, chemical engineering, and safety industries. It starts as a local desktop application with plans for a web-based version.

## Goals
- Provide affordable tools for LCA, PHA, HAZOP, etc.
- Ensure modularity, scalability, and ease of maintenance.

## Roadmap
1. **Phase 1: Local Application** (3-6 months)
   - Develop core framework and initial modules (LCA, PHA, HAZOP).
   - Test integration and document usage.
2. **Phase 2: Additional Modules** (6-12 months)
   - Add remaining modules (LOPA, What-If, etc.).
3. **Phase 3: Web Extension** (12-18 months)
   - Transition to Flask-based web app with PostgreSQL.

## Module Dependencies
- All modules rely on `src/core/` for data and UI.
- No direct dependencies between modules.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `python src/main.py`.
4. To work on a module, read its `module-plan.md`.

## Development Guidelines
- Follow `coding-standards.md`.
- Update `user-guide.md` and `developer-guide.md` in each module.