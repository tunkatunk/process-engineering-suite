"""
Logging functionality for the application.
"""
import os
import logging
from pathlib import Path
from typing import Optional

from config.settings import LOG_LEVEL, LOG_FILE, LOG_FORMAT

def setup_logger(name: str, log_file: Optional[Path] = None, 
                level: Optional[str] = None) -> logging.Logger:
    """
    Set up a logger with file and console handlers.
    
    Args:
        name: Logger name (usually __name__)
        log_file: Path to log file (defaults to settings.LOG_FILE)
        level: Logging level (defaults to settings.LOG_LEVEL)
        
    Returns:
        Configured logger
    """
    # Use defaults from settings if not provided
    if log_file is None:
        log_file = LOG_FILE
    
    if level is None:
        level_name = LOG_LEVEL
    else:
        level_name = level
    
    # Convert level name to logging level
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    log_level = level_map.get(level_name, logging.INFO)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        
        # Create formatter and add to handlers
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger for the specified name.
    
    This is a convenience function that returns a logger that's already been set up.
    If the logger hasn't been set up yet, it will be set up with default settings.
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    
    # If the logger doesn't have handlers, set it up
    if not logger.handlers:
        logger = setup_logger(name)
    
    return logger