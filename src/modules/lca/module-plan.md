# Life Cycle Analysis (LCA) Module Plan

## Overview
The LCA module helps users evaluate the environmental impact of a product or process across its life cycle (e.g., raw material extraction, manufacturing, use, disposal).

## Goals
- Enable users to define life cycle stages and associated activities.
- Calculate environmental impacts (e.g., CO2 emissions, water usage).
- Visualize and export results.

## Key Features
1. Input forms for life cycle stages and activities.
2. Predefined database of environmental impact factors.
3. Calculation engine for total impact assessment.
4. Visualization tools (e.g., bar charts, pie charts).
5. Export functionality (PDF, CSV).

## Data Requirements
- **LifeCycleStage**: ID, name, list of activities, quantities.
- **ImpactFactor**: Activity name, CO2 emissions (kg), water usage (L), energy use (kWh).

## Coding Instructions
### 1. Models (`src/models.py`)
- Define a `LifeCycleStage` class:
  - Fields: `id` (int), `name` (str), `activities` (list of dicts with activity name and quantity).
- Define an `ImpactFactor` class:
  - Fields: `activity` (str), `co2` (float), `water` (float), `energy` (float).
- Use SQLAlchemy to map these to a SQLite database via `core/data/database.py`.

### 2. Views (`src/views.py`)
- Create an `LCAView` class inheriting from `core.ui.components.FormView`:
  - Form with fields for stage name, activities, and quantities.
  - Results tab with matplotlib charts (e.g., bar chart of CO2 by stage).
- Add buttons for calculation and export.

### 3. Controllers (`src/controllers.py`)
- Implement `calculate_impact(stages: list[LifeCycleStage]) -> dict`:
  - Aggregate impacts by multiplying quantities with impact factors.
  - Return totals (e.g., {"co2": 500, "water": 1000, "energy": 2000}).
- Implement `export_results(results: dict, format: str)`:
  - Support PDF (use reportlab) and CSV (use pandas).

### 4. Entry Point (`src/main.py`)
- Use `core.ui.main_window.MainWindow` to launch the module.
- Initialize `LCAView` and add it to the main window.

### 5. Tests (`tests/`)
- `test_models.py`: Verify `LifeCycleStage` and `ImpactFactor` instantiation.
- `test_controllers.py`: Test `calculate_impact` with sample data.
- `test_views.py`: Ensure UI renders correctly (mock PyQt).

## Integration
- Use `core/data/` for database access.
- Leverage `core/ui/components.py` for forms and charts.

## Future Considerations
- Add support for external LCA databases (e.g., ecoinvent).
- Implement multiple impact assessment methods (e.g., ReCiPe).