"""
Reusable UI components and styles.
"""
from typing import Optional, List, Dict, Any, Callable

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, 
    QLineEdit, QTextEdit, QComboBox, QPushButton, QTabWidget,
    QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox,
    QGroupBox, QSpinBox, QDoubleSpinBox, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QColor, QPalette

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class FormView(QWidget):
    """Base class for form-based views."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the form view."""
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        
        # Tabs for input form and results
        self.tabs = QTabWidget()
        self.layout().addWidget(self.tabs)
        
        # Input form tab
        self.form_widget = QWidget()
        self.form_layout = QFormLayout()
        self.form_widget.setLayout(self.form_layout)
        self.tabs.addTab(self.form_widget, "Input")
        
        # Results tab
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout()
        self.results_widget.setLayout(self.results_layout)
        self.tabs.addTab(self.results_widget, "Results")
        
        # Buttons for actions
        self.buttons_layout = QHBoxLayout()
        self.layout().addLayout(self.buttons_layout)
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.on_calculate)
        self.buttons_layout.addWidget(self.calculate_button)
        
        self.export_button = QPushButton("Export")
        self.export_button.clicked.connect(self.on_export)
        self.buttons_layout.addWidget(self.export_button)
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.on_clear)
        self.buttons_layout.addWidget(self.clear_button)
    
    def add_text_field(self, label: str, placeholder: str = "") -> QLineEdit:
        """
        Add a text field to the form.
        
        Args:
            label: The label for the field
            placeholder: Optional placeholder text
            
        Returns:
            The created QLineEdit
        """
        text_edit = QLineEdit()
        text_edit.setPlaceholderText(placeholder)
        self.form_layout.addRow(label, text_edit)
        return text_edit
    
    def add_text_area(self, label: str, placeholder: str = "") -> QTextEdit:
        """
        Add a text area to the form.
        
        Args:
            label: The label for the field
            placeholder: Optional placeholder text
            
        Returns:
            The created QTextEdit
        """
        text_area = QTextEdit()
        text_area.setPlaceholderText(placeholder)
        self.form_layout.addRow(label, text_area)
        return text_area
    
    def add_dropdown(self, label: str, options: List[str]) -> QComboBox:
        """
        Add a dropdown to the form.
        
        Args:
            label: The label for the field
            options: List of options for the dropdown
            
        Returns:
            The created QComboBox
        """
        dropdown = QComboBox()
        dropdown.addItems(options)
        self.form_layout.addRow(label, dropdown)
        return dropdown
    
    def add_number_field(self, label: str, min_value: float = 0.0, 
                        max_value: float = 100.0, decimals: int = 2) -> QDoubleSpinBox:
        """
        Add a number field to the form.
        
        Args:
            label: The label for the field
            min_value: Minimum allowed value
            max_value: Maximum allowed value
            decimals: Number of decimal places
            
        Returns:
            The created QDoubleSpinBox
        """
        number_field = QDoubleSpinBox()
        number_field.setRange(min_value, max_value)
        number_field.setDecimals(decimals)
        self.form_layout.addRow(label, number_field)
        return number_field
    
    def add_checkbox(self, label: str, checked: bool = False) -> QCheckBox:
        """
        Add a checkbox to the form.
        
        Args:
            label: The label for the field
            checked: Whether the checkbox is initially checked
            
        Returns:
            The created QCheckBox
        """
        checkbox = QCheckBox()
        checkbox.setChecked(checked)
        self.form_layout.addRow(label, checkbox)
        return checkbox
    
    def on_calculate(self) -> None:
        """Handle the Calculate button click."""
        # To be implemented by subclasses
        pass
    
    def on_export(self) -> None:
        """Handle the Export button click."""
        # To be implemented by subclasses
        pass
    
    def on_clear(self) -> None:
        """Handle the Clear button click."""
        # Reset all form fields
        for i in range(self.form_layout.rowCount()):
            widget = self.form_layout.itemAt(i, QFormLayout.FieldRole).widget()
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
            elif isinstance(widget, QDoubleSpinBox):
                widget.setValue(0)
            elif isinstance(widget, QCheckBox):
                widget.setChecked(False)

class TableView(QTableWidget):
    """Enhanced table widget with additional features."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the table view."""
        super().__init__(parent)
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
    
    def set_headers(self, headers: List[str]) -> None:
        """
        Set the table headers.
        
        Args:
            headers: List of header strings
        """
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
    
    def add_row(self, row_data: List[Any]) -> None:
        """
        Add a row to the table.
        
        Args:
            row_data: List of data for the row
        """
        row = self.rowCount()
        self.insertRow(row)
        for col, data in enumerate(row_data):
            item = QTableWidgetItem(str(data))
            self.setItem(row, col, item)
    
    def clear_rows(self) -> None:
        """Clear all rows in the table."""
        self.setRowCount(0)
    
    def get_data(self) -> List[List[str]]:
        """
        Get all data from the table.
        
        Returns:
            List of rows, each a list of cell values as strings
        """
        data = []
        for row in range(self.rowCount()):
            row_data = []
            for col in range(self.columnCount()):
                item = self.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        return data

class ChartView(QWidget):
    """Widget for displaying charts and plots."""
    
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the chart view."""
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        
        # Create matplotlib figure and canvas
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.layout().addWidget(self.canvas)
        
        # Initialize with a subplot
        self.ax = self.figure.add_subplot(111)
    
    def plot_bar_chart(self, categories: List[str], values: List[float], 
                      title: str = "", xlabel: str = "", ylabel: str = "") -> None:
        """
        Create a bar chart.
        
        Args:
            categories: List of category labels
            values: List of values for each category
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label
        """
        self.ax.clear()
        self.ax.bar(categories, values)
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_xticks(range(len(categories)))
        self.ax.set_xticklabels(categories, rotation=45, ha="right")
        self.figure.tight_layout()
        self.canvas.draw()
    
    def plot_pie_chart(self, categories: List[str], values: List[float], 
                      title: str = "") -> None:
        """
        Create a pie chart.
        
        Args:
            categories: List of category labels
            values: List of values for each category
            title: Chart title
        """
        self.ax.clear()
        self.ax.pie(values, labels=categories, autopct='%1.1f%%')
        self.ax.set_title(title)
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        self.figure.tight_layout()
        self.canvas.draw()
    
    def plot_line_chart(self, x_data: List[Any], y_data: List[float], 
                       title: str = "", xlabel: str = "", ylabel: str = "") -> None:
        """
        Create a line chart.
        
        Args:
            x_data: List of x-axis values
            y_data: List of y-axis values
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label
        """
        self.ax.clear()
        self.ax.plot(x_data, y_data)
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.figure.tight_layout()
        self.canvas.draw()