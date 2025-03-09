# Life Cycle Analysis (LCA) Module - Developer Guide

## Overview

This guide provides technical information for developers working on the Life Cycle Analysis (LCA) module.

## Architecture

The LCA module follows the Model-View-Controller (MVC) pattern:

- **Models**: Data structures and database interactions (`models.py`)
- **Views**: User interface components (`views.py`)
- **Controllers**: Business logic and calculations (`controllers.py`)

## Key Components

### Models

#### `ImpactFactor`
- Represents environmental impact factors for activities
- Fields: `id`, `activity`, `co2`, `water`, `energy`

#### `LifeCycleStage`
- Represents a stage in a product or process life cycle
- Fields: `id`, `name`, `activities` (JSON string), `project_id`
- Properties: `activities_list` (converts JSON to/from Python objects)

### Views

#### `ActivityEntryWidget`
- Widget for entering an activity and its quantity
- Contains: dropdown for activity selection, input for quantity, remove button

#### `LCAView`
- Main view for the LCA module
- Inherits from core FormView
- Contains: stage name input, activities container, results display

### Controllers

#### `calculate_impact(stages)`
- Calculates environmental impact from life cycle stages
- Parameters: List of LifeCycleStage objects or dictionaries
- Returns: Dictionary of total impacts (co2, water, energy)

#### `export_results(data, format, file_path)`
- Exports results to a file (CSV or Excel)
- Parameters: Table data, export format, file path

#### `save_stage(stage, project_id)`
- Saves a stage to the database
- Parameters: Stage data dictionary, optional project ID

## Database Schema

```
lca_impact_factors
- id (PK)
- activity (STRING, unique)
- co2 (FLOAT)
- water (FLOAT)
- energy (FLOAT)

lca_stages
- id (PK)
- name (STRING)
- activities (STRING, JSON)
- project_id (FK -> projects.id)
```

## Default Data

The module uses default impact factors defined in `config/module-config/lca_config.py` when database values are not available.

## Testing

Tests are organized to match the component structure:

- `test_models.py`: Tests for data models
- `test_controllers.py`: Tests for business logic
- `test_views.py`: Tests for UI components

Run the tests with:
```
pytest src/modules/lca/tests/
```

## Integration Points

- Uses core database models (`User`, `Project`)
- Uses core UI components (`FormView`, `TableView`, `ChartView`)
- Can be extended to use external LCA databases in the future

## Future Enhancements

1. Support for external LCA databases (e.g., ecoinvent)
2. Multiple impact assessment methods (e.g., ReCiPe)
3. Graphical process flow diagram editor
4. Enhanced reporting capabilities