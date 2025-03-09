"""
Tests for the LCA module views.
"""
import pytest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication

# Create a QApplication instance for testing
app = QApplication([])

from src.modules.lca.src.views import ActivityEntryWidget, LCAView

def test_activity_entry_widget():
    """Test the ActivityEntryWidget."""
    widget = ActivityEntryWidget()
    
    # Check that the widget has the expected components
    assert widget.activity_dropdown is not None
    assert widget.quantity_input is not None
    assert widget.remove_button is not None
    
    # Test default values
    assert widget.quantity_input.value() == 1.0
    
    # Test get_activity_data method
    widget.activity_dropdown.setCurrentText("electricity_generation_coal_kwh")
    widget.quantity_input.setValue(100.0)
    data = widget.get_activity_data()
    assert data == {"activity": "electricity_generation_coal_kwh", "quantity": 100.0}

@patch('src.modules.lca.src.views.QMessageBox')
def test_lca_view(mock_messagebox):
    """Test the LCAView."""
    view = LCAView()
    
    # Check that the view has the expected components
    assert view.stage_name_input is not None
    assert view.activities_container is not None
    assert view.add_activity_button is not None
    assert view.chart_view is not None
    assert view.results_table is not None
    
    # Test add_activity method
    initial_count = view.activities_layout.count()
    view.add_activity()
    assert view.activities_layout.count() == initial_count + 1
    
    # Test get_activities method
    activities = view.get_activities()
    assert isinstance(activities, list)
    assert len(activities) > 0
    assert "activity" in activities[0]
    assert "quantity" in activities[0]
    
    # Test on_calculate method with empty stage name
    view.stage_name_input.setText("")
    view.on_calculate()
    mock_messagebox.warning.assert_called_once()
    mock_messagebox.reset_mock()
    
    # Test on_calculate method with valid input
    view.stage_name_input.setText("Manufacturing")
    
    # Mock the calculate_impact function
    with patch('src.modules.lca.src.controllers.calculate_impact') as mock_calculate:
        mock_calculate.return_value = {"co2": 100.0, "water": 200.0, "energy": 300.0}
        view.on_calculate()
        mock_calculate.assert_called_once()
    
    # Test on_export method with no results
    view.results_table.clear_rows()
    view.on_export()
    mock_messagebox.warning.assert_called_once()
    
    # Test on_clear method
    view.stage_name_input.setText("Test Stage")
    view.on_clear()
    assert view.stage_name_input.text() == ""