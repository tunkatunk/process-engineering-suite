Below is a comprehensive prompt specifically designed for Claude Code, a coding agent, to develop a modular, cost-effective software suite for process, chemical engineering, and safety industries. This prompt is exhaustive, detailing the code architecture, programming languages, folder structure, module-specific plans, and initial code snippets. It ensures modularity for each application, provides extensive documentation, and plans for future extension to a web-based platform. The setup allows Claude Code to work efficiently with limited context while supporting scalability and maintenance.

Prompt for Claude Code: Developing a Comprehensive Software Suite for Process, Chemical Engineering, and Safety Industries

Objective

You are tasked with developing a modular, cost-effective software suite tailored for process engineering, chemical engineering, and safety industries. The suite will initially include the following applications: Life Cycle Analysis (LCA), Process Hazard Analysis (PHA), HAZOP, LOPA, What-If Analyses, Process Design and Simulation, Optimization Tools, Regulatory Compliance Management, Training Modules, Data Analysis and Reporting, Incident Reporting and Analysis, and an optional AI-Assisted Analysis module. The software will start as a local desktop application with plans to extend to a web-based platform in the future. Your work must prioritize:

Modularity: Each application should function independently but integrate seamlessly via shared components.
Cost-Effectiveness: Leverage open-source tools and lightweight technologies.
Documentation: Provide extensive, clear documentation for developers and users.
Scalability: Design the architecture to support future expansion, including web deployment.
This prompt provides a detailed project structure, architecture, and initial code to get you started. Follow the instructions closely, and update the documentation as you progress.

1. Project Overview and Goals

Purpose: Deliver a suite of tools to assist engineers and safety professionals in managing process safety, environmental impact, and regulatory compliance at a lower cost than commercial alternatives.
Key Features:
Modular design for easy addition of new applications.
Local desktop application with a roadmap to a web-based platform.
Comprehensive documentation for developers and end-users.
Shared data management and UI components across modules.
Target Audience: Process engineers, chemical engineers, safety managers.
Development Approach: Use Python as the primary language, with a focus on modularity, testing, and documentation.
2. Code Architecture and Structure

The software is structured as a collection of independent modules (one per application) that share a common core for data management, UI components, and utilities. This ensures consistency, reduces redundancy, and simplifies maintenance.

2.1. Folder Structure

The project follows a hierarchical, well-organized folder structure:

plaintext

Collapse

Wrap

Copy
project-root/
│
├── docs/                         # General project documentation
│   ├── project-plan.md           # Overall project goals, roadmap, and setup (see Section 4.1)
│   ├── architecture.md           # High-level architecture overview
│   ├── coding-standards.md       # Coding guidelines and best practices
│   └── api-docs/                 # Auto-generated API documentation
│
├── src/                          # Source code for the entire suite
│   ├── core/                     # Shared functionality across modules
│   │   ├── data/                 # Data models, database setup, and ORM
│   │   │   ├── __init__.py
│   │   │   ├── models.py         # Base data models (e.g., User, Project)
│   │   │   └── database.py       # Database connection and schema
│   │   ├── ui/                   # Shared UI components and styles
│   │   │   ├── __init__.py
│   │   │   ├── main_window.py    # Main application window
│   │   │   └── components.py     # Reusable UI elements (e.g., forms, charts)
│   │   └── utils/                # Utility functions
│   │       ├── __init__.py
│   │       ├── logger.py         # Logging functionality
│   │       └── validators.py     # Input validation helpers
│   │
│   ├── modules/                  # Individual application modules
│   │   ├── lca/                  # Life Cycle Analysis module
│   │   │   ├── module-plan.md    # Detailed plan for LCA (see Section 3.2.1)
│   │   │   ├── src/              # Source code
│   │   │   │   ├── __init__.py
│   │   │   │   ├── main.py       # Module entry point
│   │   │   │   ├── models.py     # LCA-specific models
│   │   │   │   ├── views.py      # UI components
│   │   │   │   └── controllers.py # Business logic
│   │   │   ├── tests/            # Unit and integration tests
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   └── test_controllers.py
│   │   │   └── docs/             # Module-specific documentation
│   │   │       ├── user-guide.md
│   │   │       └── developer-guide.md
│   │   │
│   │   ├── pha/                  # Process Hazard Analysis module (similar structure)
│   │   ├── hazop/                # HAZOP module (similar structure)
│   │   ├── lopa/                 # LOPA module (similar structure)
│   │   ├── what-if/              # What-If Analysis module (similar structure)
│   │   ├── process-design/       # Process Design and Simulation module (similar structure)
│   │   ├── optimization/         # Optimization Tools module (similar structure)
│   │   ├── compliance/           # Regulatory Compliance Management module (similar structure)
│   │   ├── training/             # Training Modules (similar structure)
│   │   ├── data-analysis/        # Data Analysis and Reporting module (similar structure)
│   │   ├── incident-reporting/   # Incident Reporting and Analysis module (similar structure)
│   │   └── ai-analysis/          # AI-Assisted Analysis module (optional, similar structure)
│   │
│   └── main.py                   # Entry point for the entire application
│
├── tests/                        # Global integration and end-to-end tests
│   ├── test_integration.py
│   └── test_end_to_end.py
│
├── config/                       # Configuration files
│   ├── settings.py               # Global settings (e.g., database path, log level)
│   └── module-config/            # Module-specific configurations
│       ├── lca_config.py
│       └── [other modules].py
│
├── scripts/                      # Automation scripts
│   ├── build.sh                  # Build script
│   ├── test.sh                   # Test runner
│   └── deploy.sh                 # Deployment script (placeholder for web)
│
├── requirements.txt              # Python dependencies
│
└── README.md                     # Quick setup instructions and project overview
docs/: Stores high-level project documentation (see Section 4).
src/core/: Contains reusable components (data models, UI, utilities).
src/modules/: Houses individual modules, each with its own module-plan.md, source code, tests, and documentation.
tests/: Global tests to verify module integration.
config/: Settings for the application and modules.
scripts/: Scripts for automation (building, testing, deploying).
2.2. Programming Languages and Technologies

Primary Language: Python 3.9+ (for scientific computing, data analysis, and AI integration).
UI Framework: PyQt5 (cross-platform, robust for desktop applications).
Database: SQLite (lightweight, local storage); use SQLAlchemy as an ORM for future database flexibility (e.g., PostgreSQL for web).
Web Framework (Future): Flask (lightweight, suitable for RESTful APIs).
Testing: Pytest (unit and integration testing).
Documentation: Sphinx (API docs), Markdown (user/developer guides).
Dependencies (in requirements.txt):
text

Collapse

Wrap

Copy
pyqt5==5.15.7
sqlalchemy==1.4.40
pytest==7.4.0
sphinx==5.3.0
matplotlib==3.7.2  # For charts and visualizations
pandas==2.0.3      # For data analysis
2.3. Modular Design Principles

Separation of Concerns: Use the MVC (Model-View-Controller) pattern within each module:
Models: Data structures and database interactions.
Views: UI components.
Controllers: Business logic and calculations.
API-First Approach: Design each module with a clear internal API (e.g., functions/classes) that can later be exposed as RESTful endpoints.
Shared Core: Use src/core/ for common functionality (e.g., database access, UI templates).
Configuration: Store settings in config/ to allow customization without code changes.
3. Module Design and Plans

Each module is an independent application with a consistent structure. Below is the general structure, followed by a detailed example for the LCA module.

3.1. General Module Structure

Each module folder (e.g., src/modules/lca/) contains:

plaintext

Collapse

Wrap

Copy
module-name/
├── module-plan.md       # Detailed instructions for Claude Code (see examples below)
├── src/                 # Source code
│   ├── __init__.py
│   ├── main.py          # Module entry point
│   ├── models.py        # Data models specific to the module
│   ├── views.py         # UI components
│   └── controllers.py   # Business logic
├── tests/               # Module-specific tests
│   ├── test_models.py
│   ├── test_views.py
│   └── test_controllers.py
└── docs/                # Module-specific documentation
    ├── user-guide.md    # How to use the module
    └── developer-guide.md # Technical details for developers
3.2. Example Module Plans

Below are detailed module-plan.md examples for two modules: LCA and HAZOP. Other modules follow a similar pattern.

3.2.1. LCA Module Plan (src/modules/lca/module-plan.md)
markdown

Collapse

Wrap

Copy
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
3.2.2. HAZOP Module Plan (src/modules/hazop/module-plan.md)
markdown

Collapse

Wrap

Copy
# HAZOP Module Plan

## Overview
The HAZOP module supports Hazard and Operability studies by guiding users through a structured risk assessment of process deviations.

## Goals
- Facilitate identification of hazards in process systems.
- Document deviations, causes, consequences, and safeguards.

## Key Features
1. Input forms for process nodes, parameters, and guidewords (e.g., "More", "Less").
2. Table to record deviations, causes, consequences, and safeguards.
3. Risk ranking (e.g., severity × likelihood).
4. Report generation (PDF).

## Data Requirements
- **Node**: ID, name, description.
- **Deviation**: Node ID, parameter, guideword, cause, consequence, safeguard, risk score.

## Coding Instructions
### 1. Models (`src/models.py`)
- Define a `Node` class: `id` (int), `name` (str), `description` (str).
- Define a `Deviation` class: `node_id` (int), `parameter` (str), `guideword` (str), `cause` (str), `consequence` (str), `safeguard` (str), `risk_score` (int).

### 2. Views (`src/views.py`)
- Create a `HAZOPView` class:
  - Form for node details.
  - Table widget for deviations (editable).
  - Risk visualization (e.g., heatmap).

### 3. Controllers (`src/controllers.py`)
- Implement `calculate_risk(severity: int, likelihood: int) -> int`:
  - Return severity × likelihood.
- Implement `generate_report(deviations: list[Deviation])`:
  - Create a PDF report with node and deviation details.

### 4. Entry Point (`src/main.py`)
- Launch via `core.ui.main_window.MainWindow`.

### 5. Tests (`tests/`)
- Test model creation, risk calculation, and UI rendering.

## Integration
- Use shared database and UI components from `core/`.

## Future Considerations
- Add templates for common industries (e.g., oil and gas).
- Integrate with LOPA for layered risk analysis.
Note: Other modules (e.g., PHA, LOPA) follow a similar structure. Create a module-plan.md for each with specific features, data models, and instructions tailored to their purpose.

4. Documentation

Documentation is split into general project-level and module-specific files.

4.1. General Project Documentation

docs/project-plan.md (in root docs/):
markdown

Collapse

Wrap

Copy
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
docs/architecture.md:
Diagram of modular structure (core + modules).
Data flow: User → UI → Controller → Models → Database.
docs/coding-standards.md:
PEP 8 formatting, docstrings for all functions/classes, type hints.
4.2. Module-Specific Documentation

user-guide.md: Step-by-step usage instructions with screenshots.
developer-guide.md: Technical details (architecture, key functions, testing).
5. Extending to a Web Application

To prepare for future web deployment:

API Design: Write module controllers with clear function signatures (e.g., calculate_impact(inputs) -> dict) that can become REST endpoints.
Database: Use SQLAlchemy for database abstraction (SQLite now, PostgreSQL later).
UI Separation: Keep UI code in views.py separate from logic in controllers.py.
Configurability: Store settings (e.g., database URL) in config/settings.py.
6. Initial Code Setup

Below are starting code snippets for Claude Code to build upon.

6.1. Core Data Model (src/core/data/models.py)

python

Collapse

Wrap

Copy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """Base user model for authentication."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    role = Column(String)  # e.g., "engineer", "admin"
6.2. Core UI Component (src/core/ui/main_window.py)

python

Collapse

Wrap

Copy
from PyQt5.QtWidgets import QMainWindow, QTabWidget

class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process & Safety Suite")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
    
    def add_module(self, view):
        """Add a module's view as a tab."""
        self.tabs.addTab(view, view.__class__.__name__)
    
    def run(self):
        self.show()
6.3. Application Entry Point (src/main.py)

python

Collapse

Wrap

Copy
import sys
from PyQt5.QtWidgets import QApplication
from core.ui.main_window import MainWindow
from modules.lca.src.main import run_lca_module

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    run_lca_module(window)  # Example: Launch LCA module
    sys.exit(app.exec_())
6.4. LCA Module Example (src/modules/lca/src/models.py)

python

Collapse

Wrap

Copy
from sqlalchemy import Column, Integer, String, Float
from core.data.models import Base

class LifeCycleStage(Base):
    __tablename__ = "lca_stages"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    activities = Column(String)  # JSON string of activities and quantities
7. Instructions for Claude Code

Setup:
Clone the repository.
Install dependencies: pip install -r requirements.txt.
Read docs/project-plan.md for context.
Development:
Choose a module (e.g., src/modules/lca/).
Read its module-plan.md for specific tasks.
Implement features using core/ components.
Testing:
Write tests in tests/ for each module.
Run tests: pytest tests/.
Documentation:
Update docs/ files as you add features.
8. Conclusion

This prompt provides a detailed, structured framework for you, Claude Code, to develop a modular software suite. The architecture supports independent module development, extensive documentation ensures clarity, and the design prepares for future web expansion. Start with the LCA module, then proceed to others, updating documentation along the way. Refer to project-plan.md each time you begin a session to stay aligned with the project’s goals.