# Software Architecture

## Overview

The software is structured as a collection of independent modules (one per application) that share a common core for data management, UI components, and utilities. This ensures consistency, reduces redundancy, and simplifies maintenance.

## High-Level Architecture

```
User Interface (PyQt5)
      │
      ▼
 Controllers (Business Logic)
      │
      ▼
   Models (Data)
      │
      ▼
  Database (SQLite/SQLAlchemy)
```

## Core Components

### Data Layer
- Uses SQLAlchemy as ORM
- Base models defined in `core/data/models.py`
- Database connection handled in `core/data/database.py`

### UI Layer
- Built with PyQt5
- Main window defined in `core/ui/main_window.py`
- Reusable components in `core/ui/components.py`

### Utils
- Logging functionality in `utils/logger.py`
- Input validation in `utils/validators.py`

## Module Structure

Each module follows the Model-View-Controller (MVC) pattern:

- **Models**: Data structures and database interactions
- **Views**: UI components
- **Controllers**: Business logic and calculations

## Extension to Web

Future web deployment preparation:

- Clear API function signatures in module controllers
- Database abstraction via SQLAlchemy
- UI separation (views.py separate from controllers.py)
- Configuration management in config/settings.py