"""
Global settings for the application.
"""
from pathlib import Path
import os

# Base directories
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = PROJECT_ROOT / "src"
MODULES_DIR = SRC_DIR / "modules"

# Database settings
DATABASE = {
    "dialect": "sqlite",
    "name": "app.db",
    "path": PROJECT_ROOT / "data"
}
DATABASE_URI = f"{DATABASE['dialect']}:///{DATABASE['path']}/{DATABASE['name']}"

# Logging settings
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = PROJECT_ROOT / "logs" / "app.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# UI settings
APPLICATION_NAME = "Process & Safety Suite"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
THEME = "light"  # Options: light, dark

# Module settings
ENABLED_MODULES = [
    "lca",
    "pha",
    "hazop"
    # Add other modules as they are developed
]

# Development mode (set to False in production)
DEBUG = True