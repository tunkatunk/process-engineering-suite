"""
Entry point for the LCA module.
"""
from PyQt5.QtWidgets import QWidget

from core.ui.main_window import MainWindow
from core.utils.logger import get_logger
from views import LCAView

# Set up logger
logger = get_logger(__name__)

def run_module(window: MainWindow) -> None:
    """
    Run the LCA module.
    
    Args:
        window: The main application window
    """
    logger.info("Starting LCA module")
    
    # Create the module view
    lca_view = LCAView()
    
    # Add the view to the main window
    window.add_module(lca_view, "Life Cycle Analysis")
    
    logger.info("LCA module started")