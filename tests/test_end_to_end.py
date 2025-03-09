"""
End-to-end tests for the application.
"""
import os
import sys
import pytest
from unittest.mock import patch
from PyQt5.QtWidgets import QApplication

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create a QApplication instance for testing
app = QApplication([])

from src.core.data.database import init_db
from src.core.ui.main_window import MainWindow
from src.modules.lca.src.views import LCAView

@pytest.fixture
def setup_database():
    """Set up the test database."""
    # Use in-memory database for testing
    os.environ["DATABASE_URI"] = "sqlite:///:memory:"
    init_db()
    yield
    # No need to clean up in-memory database

@pytest.fixture
def main_window():
    """Create a main window for testing."""
    return MainWindow()

def test_app_startup(setup_database, main_window):
    """Test that the application starts up correctly."""
    assert main_window.windowTitle() == "Process & Safety Suite"
    assert main_window.tabs is not None

def test_lca_module_integration(setup_database, main_window):
    """Test that the LCA module integrates with the main window."""
    # Create and add the LCA view
    lca_view = LCAView()
    main_window.add_module(lca_view, "Life Cycle Analysis")
    
    # Check that the view was added as a tab
    assert main_window.tabs.count() == 1
    assert main_window.tabs.tabText(0) == "Life Cycle Analysis"
    
    # Test interaction between view and controller
    with patch('src.modules.lca.src.controllers.calculate_impact') as mock_calculate:
        # Set up mock return value
        mock_calculate.return_value = {"co2": 750.0, "water": 6000.0, "energy": 3000.0}
        
        # Fill in the form
        lca_view.stage_name_input.setText("Manufacturing")
        
        # Get the activities widget
        activity_widget = None
        for i in range(lca_view.activities_layout.count()):
            widget = lca_view.activities_layout.itemAt(i).widget()
            if widget:
                activity_widget = widget
                break
        
        assert activity_widget is not None
        
        # Set activity values
        activity_widget.activity_dropdown.setCurrentText("electricity_generation_coal_kwh")
        activity_widget.quantity_input.setValue(500.0)
        
        # Calculate
        lca_view.on_calculate()
        
        # Check that calculate_impact was called with the right data
        mock_calculate.assert_called_once()
        args = mock_calculate.call_args[0][0]
        assert len(args) == 1
        assert args[0]["name"] == "Manufacturing"
        assert args[0]["activities"][0]["activity"] == "electricity_generation_coal_kwh"
        assert args[0]["activities"][0]["quantity"] == 500.0

def test_multiple_modules(setup_database, main_window):
    """Test adding multiple modules to the main window."""
    # Add the same module type twice (in a real app, these would be different module types)
    lca_view1 = LCAView()
    lca_view2 = LCAView()
    
    main_window.add_module(lca_view1, "Life Cycle Analysis 1")
    main_window.add_module(lca_view2, "Life Cycle Analysis 2")
    
    # Check that both were added as tabs
    assert main_window.tabs.count() == 2
    assert main_window.tabs.tabText(0) == "Life Cycle Analysis 1"
    assert main_window.tabs.tabText(1) == "Life Cycle Analysis 2"
    
    # Test closing a tab
    main_window.close_tab(0)
    assert main_window.tabs.count() == 1
    assert main_window.tabs.tabText(0) == "Life Cycle Analysis 2"