"""
Main application window with tabbed interface.
"""
from typing import Optional, List

from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QMenuBar, QStatusBar, 
    QAction, QToolBar, QMessageBox, QFileDialog, QDockWidget
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from config.settings import APPLICATION_NAME, WINDOW_WIDTH, WINDOW_HEIGHT

class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""
    
    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle(APPLICATION_NAME)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Set up the central widget (tabbed interface)
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)
        
        # Set up the menu bar
        self._create_menu_bar()
        
        # Set up the status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Set up the tool bar
        self._create_tool_bar()
    
    def _create_menu_bar(self) -> None:
        """Create the menu bar with actions."""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("&File")
        
        new_action = QAction("&New Project", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._on_new_project)
        file_menu.addAction(new_action)
        
        open_action = QAction("&Open Project", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._on_open_project)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Modules menu
        modules_menu = menu_bar.addMenu("&Modules")
        
        # Add actions for each module
        # These will be populated dynamically based on available modules
        
        # Help menu
        help_menu = menu_bar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self._on_about)
        help_menu.addAction(about_action)
    
    def _create_tool_bar(self) -> None:
        """Create the main toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        # Add actions to toolbar
        # These will be populated with icons for common operations
    
    def add_module(self, view, title: str) -> None:
        """
        Add a module's view as a tab.
        
        Args:
            view: The module's view widget
            title: The tab title
        """
        self.tabs.addTab(view, title)
        self.tabs.setCurrentWidget(view)
    
    def close_tab(self, index: int) -> None:
        """
        Close a tab.
        
        Args:
            index: The index of the tab to close
        """
        # Ask for confirmation if the tab has unsaved changes
        # For now, just close the tab
        self.tabs.removeTab(index)
    
    def _on_new_project(self) -> None:
        """Handle the New Project action."""
        # To be implemented: open a dialog to create a new project
        self.status_bar.showMessage("Creating a new project...")
    
    def _on_open_project(self) -> None:
        """Handle the Open Project action."""
        # To be implemented: open a dialog to open an existing project
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Project Files (*.proj)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.status_bar.showMessage(f"Opening project: {selected_files[0]}")
    
    def _on_about(self) -> None:
        """Handle the About action."""
        QMessageBox.about(
            self,
            "About Process & Safety Suite",
            f"{APPLICATION_NAME}\n\n"
            "A modular software suite for process engineering, chemical engineering, and safety industries."
        )
    
    def run(self) -> None:
        """Show the main window."""
        self.show()