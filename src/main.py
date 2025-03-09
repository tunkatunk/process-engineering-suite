"""
Entry point for the entire application.
"""
import sys
import os
import importlib
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from core.ui.main_window import MainWindow
from core.data.database import init_db
from core.utils.logger import get_logger
from config.settings import ENABLED_MODULES, SRC_DIR, MODULES_DIR

# Set up logger
logger = get_logger(__name__)

def import_module(module_name: str):
    """
    Dynamically import a module.
    
    Args:
        module_name: Name of the module to import
        
    Returns:
        The imported module or None if import fails
    """
    try:
        module_path = f"modules.{module_name}.src.main"
        module = importlib.import_module(module_path)
        logger.info(f"Successfully imported {module_path}")
        return module
    except ImportError as e:
        logger.error(f"Failed to import {module_path}: {e}")
        return None

def run_module(module, window: MainWindow):
    """
    Run a module's main function.
    
    Args:
        module: The module to run
        window: The main window to add the module to
        
    Returns:
        True if the module was run successfully, False otherwise
    """
    try:
        if hasattr(module, 'run_module'):
            module.run_module(window)
            return True
        else:
            logger.error(f"Module {module.__name__} does not have a run_module function")
            return False
    except Exception as e:
        logger.error(f"Error running module {module.__name__}: {e}")
        return False

def main():
    """Main entry point for the application."""
    # Initialize the database
    init_db()
    
    # Create the QApplication instance
    app = QApplication(sys.argv)
    
    # Create the main window
    window = MainWindow()
    
    # Load enabled modules
    loaded_modules = 0
    for module_name in ENABLED_MODULES:
        module = import_module(module_name)
        if module:
            if run_module(module, window):
                loaded_modules += 1
    
    logger.info(f"Loaded {loaded_modules} modules")
    
    if loaded_modules == 0:
        logger.warning("No modules were loaded")
    
    # Show the main window
    window.run()
    
    # Start the event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()