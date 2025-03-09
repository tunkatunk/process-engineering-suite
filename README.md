# Process, Chemical Engineering, and Safety Software Suite

A modular, cost-effective software suite for process engineering, chemical engineering, and safety industries.

## Overview

This project delivers a suite of tools to assist engineers and safety professionals in managing process safety, environmental impact, and regulatory compliance at a lower cost than commercial alternatives.

## Key Features

- **Modular Design**: Each application functions independently but integrates seamlessly
- **Cost-Effective**: Built with open-source tools and technologies
- **Extensive Documentation**: Clear documentation for developers and users
- **Scalable Architecture**: Designed to support future expansion, including web deployment

## Modules

The suite includes the following modules:

- **Life Cycle Analysis (LCA)**: Evaluate environmental impact across product or process life cycles
- **Process Hazard Analysis (PHA)**: Identify and assess process hazards
- **HAZOP**: Conduct hazard and operability studies
- **LOPA**: Perform layer of protection analysis
- **What-If Analyses**: Explore potential process deviations
- **Process Design and Simulation**: Design and simulate process systems
- **Optimization Tools**: Optimize process parameters
- **Regulatory Compliance Management**: Track and manage regulatory requirements
- **Training Modules**: Provide training on safety procedures
- **Data Analysis and Reporting**: Analyze and report on process data
- **Incident Reporting and Analysis**: Document and analyze incidents
- **AI-Assisted Analysis**: Apply AI to enhance analysis (optional)

## Technology Stack

- **Backend**: Python 3.9+
- **UI Framework**: PyQt5
- **Database**: SQLite with SQLAlchemy ORM
- **Data Analysis**: Pandas, Matplotlib
- **Testing**: pytest

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Supreme-App
   ```

2. Run the build script:
   ```
   ./scripts/build.sh
   ```

3. Start the application:
   ```
   python src/main.py
   ```

## Development

### Project Structure

The project follows a modular architecture:

- `core/`: Shared functionality (database, UI, utilities)
- `modules/`: Individual application modules, each with MVC structure
- `config/`: Configuration settings
- `docs/`: Documentation
- `scripts/`: Build and deployment scripts
- `tests/`: Global integration tests

### Running Tests

Run all tests:
```
./scripts/test.sh
```

Run tests for a specific module:
```
./scripts/test.sh -m lca
```

Run a specific test file:
```
./scripts/test.sh -t src/modules/lca/tests/test_models.py
```

## Documentation

- `docs/project-plan.md`: Overall project goals and roadmap
- `docs/architecture.md`: Architecture overview
- `docs/coding-standards.md`: Coding guidelines
- Each module has its own documentation in `src/modules/<module>/docs/`

## Future Development

- Add remaining modules
- Enhance existing modules with additional features
- Transition to a web-based platform using Flask

## License

[License information goes here]