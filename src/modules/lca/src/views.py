"""
UI components for the LCA module.
"""
from typing import List, Dict, Any, Optional

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, 
    QTableWidget, QTableWidgetItem, QComboBox, QLineEdit,
    QSpinBox, QDoubleSpinBox, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt

from core.ui.components import FormView, TableView, ChartView
from config.module_config.lca_config import DEFAULT_IMPACT_FACTORS

class ActivityEntryWidget(QWidget):
    """Widget for entering an activity and its quantity."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the widget."""
        super().__init__(parent)
        self.setLayout(QHBoxLayout())
        
        # Activity dropdown
        self.activity_dropdown = QComboBox()
        self.activity_dropdown.addItems(sorted(DEFAULT_IMPACT_FACTORS.keys()))
        self.layout().addWidget(self.activity_dropdown)
        
        # Quantity input
        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setRange(0.01, 1000000)
        self.quantity_input.setValue(1.0)
        self.quantity_input.setDecimals(2)
        self.layout().addWidget(self.quantity_input)
        
        # Remove button
        self.remove_button = QPushButton("Remove")
        self.remove_button.clicked.connect(self.on_remove)
        self.layout().addWidget(self.remove_button)
    
    def on_remove(self) -> None:
        """Handle the Remove button click."""
        # Remove this widget from its parent
        if self.parent():
            layout = self.parent().layout()
            layout.removeWidget(self)
            self.deleteLater()
    
    def get_activity_data(self) -> Dict[str, Any]:
        """
        Get the activity and quantity.
        
        Returns:
            Dictionary with keys 'activity' and 'quantity'
        """
        return {
            "activity": self.activity_dropdown.currentText(),
            "quantity": self.quantity_input.value()
        }

class LCAView(FormView):
    """Main view for the LCA module."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the view."""
        super().__init__(parent)
        self.setWindowTitle("Life Cycle Analysis")
        
        # Add stage name field
        self.stage_name_input = self.add_text_field("Stage Name", "Enter stage name")
        
        # Container for activities
        self.activities_container = QWidget()
        self.activities_layout = QVBoxLayout()
        self.activities_container.setLayout(self.activities_layout)
        self.form_layout.addRow("Activities", self.activities_container)
        
        # Add initial activity
        self.add_activity()
        
        # Add button to add more activities
        self.add_activity_button = QPushButton("Add Activity")
        self.add_activity_button.clicked.connect(self.add_activity)
        self.form_layout.addRow("", self.add_activity_button)
        
        # Set up results tab
        self.chart_view = ChartView()
        self.results_layout.addWidget(self.chart_view)
        
        self.results_table = TableView()
        self.results_table.set_headers(["Stage", "CO2 (kg)", "Water (L)", "Energy (kWh)"])
        self.results_layout.addWidget(self.results_table)
    
    def add_activity(self) -> None:
        """Add an activity entry widget."""
        activity_widget = ActivityEntryWidget()
        self.activities_layout.addWidget(activity_widget)
    
    def get_activities(self) -> List[Dict[str, Any]]:
        """
        Get all activities and quantities.
        
        Returns:
            List of dictionaries with keys 'activity' and 'quantity'
        """
        activities = []
        
        # Get data from each activity widget
        for i in range(self.activities_layout.count()):
            widget = self.activities_layout.itemAt(i).widget()
            if isinstance(widget, ActivityEntryWidget):
                activities.append(widget.get_activity_data())
        
        return activities
    
    def on_calculate(self) -> None:
        """Handle the Calculate button click."""
        # Get the stage name
        stage_name = self.stage_name_input.text()
        if not stage_name:
            QMessageBox.warning(self, "Warning", "Please enter a stage name")
            return
        
        # Get the activities
        activities = self.get_activities()
        if not activities:
            QMessageBox.warning(self, "Warning", "Please add at least one activity")
            return
        
        # Create a stage
        stage = {
            "name": stage_name,
            "activities": activities
        }
        
        # Calculate impacts
        try:
            from controllers import calculate_impact
            results = calculate_impact([stage])
            
            # Display results
            self.display_results(results, [stage])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error calculating impacts: {e}")
    
    def display_results(self, results: Dict[str, float], stages: List[Dict[str, Any]]) -> None:
        """
        Display the results in the results tab.
        
        Args:
            results: Dictionary with total impacts
            stages: List of stage dictionaries
        """
        # Switch to results tab
        self.tabs.setCurrentIndex(1)
        
        # Clear previous results
        self.results_table.clear_rows()
        
        # Add totals to table
        self.results_table.add_row(["Total", 
                                    f"{results['co2']:.2f}", 
                                    f"{results['water']:.2f}", 
                                    f"{results['energy']:.2f}"])
        
        # Create chart
        self.chart_view.plot_pie_chart(
            ["CO2 (kg)", "Water (L)", "Energy (kWh)"],
            [results["co2"], results["water"] / 10, results["energy"]],  # Scale water for better visualization
            "Environmental Impact Distribution"
        )
    
    def on_export(self) -> None:
        """Handle the Export button click."""
        # Check if there are results to export
        if self.results_table.rowCount() == 0:
            QMessageBox.warning(self, "Warning", "Please calculate results first")
            return
        
        # Ask for file location
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("CSV Files (*.csv);;Excel Files (*.xlsx)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            file_format = "csv" if file_path.endswith(".csv") else "xlsx"
            
            try:
                from controllers import export_results
                # Get data from table
                data = self.results_table.get_data()
                export_results(data, file_format, file_path)
                QMessageBox.information(self, "Success", f"Results exported to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error exporting results: {e}")
    
    def on_clear(self) -> None:
        """Handle the Clear button click."""
        # Clear stage name
        self.stage_name_input.clear()
        
        # Clear activities
        for i in reversed(range(self.activities_layout.count())):
            widget = self.activities_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        
        # Add one empty activity
        self.add_activity()