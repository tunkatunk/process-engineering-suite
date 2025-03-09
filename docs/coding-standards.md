# Coding Standards

## General Guidelines

- Follow PEP 8 for Python code formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use docstrings for all public functions, classes, and methods

## Naming Conventions

- **Classes**: CamelCase (e.g., `LifeCycleStage`)
- **Functions and variables**: snake_case (e.g., `calculate_impact`)
- **Constants**: UPPER_CASE_WITH_UNDERSCORES (e.g., `MAX_ITERATIONS`)
- **Private methods/attributes**: prefix with underscore (e.g., `_calculate_internal_value`)

## Imports

Organize imports in this order, with a blank line between groups:
1. Standard library imports
2. Third-party library imports
3. Local application imports

Example:
```python
import os
import sys
from typing import List, Dict, Optional

import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication

from core.data.models import Base
from core.utils.logger import setup_logger
```

## Type Hints

- Use type hints for all function arguments and return values
- Import typing module for complex types (List, Dict, Optional, etc.)

Example:
```python
def calculate_impact(stages: List[LifeCycleStage]) -> Dict[str, float]:
    """Calculate environmental impact from life cycle stages."""
    results = {"co2": 0.0, "water": 0.0, "energy": 0.0}
    # Implementation
    return results
```

## Documentation

- Use docstrings for all public classes, methods, and functions
- Include parameter descriptions and return value descriptions
- Document exceptions that might be raised

Example:
```python
def validate_input(value: float, min_val: float = 0.0, max_val: float = 100.0) -> bool:
    """
    Validate that a value is within the specified range.
    
    Args:
        value: The value to validate
        min_val: Minimum acceptable value (default: 0.0)
        max_val: Maximum acceptable value (default: 100.0)
        
    Returns:
        True if value is within range, False otherwise
        
    Raises:
        TypeError: If value is not a number
    """
```

## Error Handling

- Use specific exceptions rather than generic ones
- Provide meaningful error messages
- Handle exceptions at appropriate levels

## Testing

- Write tests for all functions and classes
- Organize tests to mirror the module structure
- Use appropriate fixtures and mocks
- Aim for at least 80% code coverage