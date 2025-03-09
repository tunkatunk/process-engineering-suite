"""
Input validation helpers.
"""
import re
from typing import Any, List, Dict, Optional, Union, Tuple

def validate_required(value: Any) -> Tuple[bool, str]:
    """
    Validate that a value is not None or empty.
    
    Args:
        value: The value to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if value is None:
        return False, "This field is required"
    
    if isinstance(value, str) and value.strip() == "":
        return False, "This field is required"
    
    if isinstance(value, (list, dict)) and len(value) == 0:
        return False, "This field is required"
    
    return True, ""

def validate_number(value: Any, min_value: Optional[float] = None, 
                   max_value: Optional[float] = None) -> Tuple[bool, str]:
    """
    Validate that a value is a number within the specified range.
    
    Args:
        value: The value to validate
        min_value: Optional minimum value
        max_value: Optional maximum value
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check if the value is a number
    try:
        num_value = float(value)
    except (ValueError, TypeError):
        return False, "Must be a number"
    
    # Check if the value is within the specified range
    if min_value is not None and num_value < min_value:
        return False, f"Must be at least {min_value}"
    
    if max_value is not None and num_value > max_value:
        return False, f"Must be at most {max_value}"
    
    return True, ""

def validate_email(value: str) -> Tuple[bool, str]:
    """
    Validate that a value is a valid email address.
    
    Args:
        value: The value to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(value, str):
        return False, "Email must be a string"
    
    # Simple email regex pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(pattern, value):
        return True, ""
    else:
        return False, "Invalid email address"

def validate_length(value: str, min_length: Optional[int] = None, 
                   max_length: Optional[int] = None) -> Tuple[bool, str]:
    """
    Validate that a string has the specified length.
    
    Args:
        value: The value to validate
        min_length: Optional minimum length
        max_length: Optional maximum length
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(value, str):
        return False, "Value must be a string"
    
    length = len(value)
    
    if min_length is not None and length < min_length:
        return False, f"Must be at least {min_length} characters"
    
    if max_length is not None and length > max_length:
        return False, f"Must be at most {max_length} characters"
    
    return True, ""

def validate_pattern(value: str, pattern: str, 
                    error_message: str = "Invalid format") -> Tuple[bool, str]:
    """
    Validate that a string matches the specified regex pattern.
    
    Args:
        value: The value to validate
        pattern: Regex pattern to match
        error_message: Error message to return if validation fails
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(value, str):
        return False, "Value must be a string"
    
    if re.match(pattern, value):
        return True, ""
    else:
        return False, error_message

def validate_list_items(items: List[Any], validator_func, 
                       *args, **kwargs) -> List[Tuple[bool, str]]:
    """
    Validate each item in a list using the specified validator function.
    
    Args:
        items: List of items to validate
        validator_func: Function to validate each item
        *args, **kwargs: Additional arguments to pass to the validator function
        
    Returns:
        List of (is_valid, error_message) tuples, one for each item
    """
    return [validator_func(item, *args, **kwargs) for item in items]

def validate_all(validations: List[Tuple[bool, str]]) -> Tuple[bool, List[str]]:
    """
    Check if all validations passed and collect error messages.
    
    Args:
        validations: List of (is_valid, error_message) tuples
        
    Returns:
        Tuple of (all_valid, error_messages)
    """
    all_valid = all(valid for valid, _ in validations)
    error_messages = [message for valid, message in validations if not valid]
    return all_valid, error_messages