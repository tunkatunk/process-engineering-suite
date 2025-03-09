"""
Business logic for the LCA module.
"""
from typing import List, Dict, Any, Optional, Union
import json
import os
from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session

from core.data.database import get_db
from core.utils.logger import get_logger
from models import LifeCycleStage, ImpactFactor
from config.module_config.lca_config import DEFAULT_IMPACT_FACTORS

# Set up logger
logger = get_logger(__name__)

def get_impact_factors(db: Optional[Session] = None) -> Dict[str, Dict[str, float]]:
    """
    Get all impact factors from the database or defaults.
    
    Args:
        db: Optional database session
        
    Returns:
        Dictionary mapping activity names to impact dictionaries
    """
    # If db is None, use default factors
    if db is None:
        return {
            activity: {
                "co2": factors[0],
                "water": factors[1],
                "energy": factors[2]
            }
            for activity, factors in DEFAULT_IMPACT_FACTORS.items()
        }
    
    # Otherwise, get factors from database
    try:
        impact_factors = db.query(ImpactFactor).all()
        return {
            factor.activity: {
                "co2": factor.co2,
                "water": factor.water,
                "energy": factor.energy
            }
            for factor in impact_factors
        }
    except Exception as e:
        logger.error(f"Error getting impact factors from database: {e}")
        # Fall back to defaults
        return {
            activity: {
                "co2": factors[0],
                "water": factors[1],
                "energy": factors[2]
            }
            for activity, factors in DEFAULT_IMPACT_FACTORS.items()
        }

def calculate_impact(stages: List[Union[LifeCycleStage, Dict[str, Any]]]) -> Dict[str, float]:
    """
    Calculate environmental impact from life cycle stages.
    
    Args:
        stages: List of LifeCycleStage objects or dictionaries
        
    Returns:
        Dictionary of total impacts (co2, water, energy)
    """
    # Get impact factors
    impact_factors = get_impact_factors()
    
    # Initialize results
    results = {"co2": 0.0, "water": 0.0, "energy": 0.0}
    
    # Calculate impact for each stage
    for stage in stages:
        # Get activities from stage
        if isinstance(stage, LifeCycleStage):
            activities = stage.activities_list
        else:
            activities = stage.get("activities", [])
        
        # Calculate impact for each activity
        for activity_data in activities:
            activity_name = activity_data.get("activity")
            quantity = float(activity_data.get("quantity", 1.0))
            
            # Look up impact factors
            if activity_name in impact_factors:
                factors = impact_factors[activity_name]
                results["co2"] += factors["co2"] * quantity
                results["water"] += factors["water"] * quantity
                results["energy"] += factors["energy"] * quantity
            else:
                logger.warning(f"Impact factors not found for activity: {activity_name}")
    
    return results

def export_results(data: List[List[str]], format: str, file_path: str) -> None:
    """
    Export results to a file.
    
    Args:
        data: Table data as a list of rows (each row is a list of cell values)
        format: Export format ('csv' or 'xlsx')
        file_path: Path to save the file
    """
    # Create a DataFrame from the data
    headers = ["Stage", "CO2 (kg)", "Water (L)", "Energy (kWh)"]
    df = pd.DataFrame(data, columns=headers)
    
    # Export based on format
    if format.lower() == "csv":
        df.to_csv(file_path, index=False)
    elif format.lower() == "xlsx":
        df.to_excel(file_path, index=False)
    else:
        raise ValueError(f"Unsupported export format: {format}")
    
    logger.info(f"Exported results to {file_path}")

def save_stage(stage: Dict[str, Any], project_id: Optional[int] = None) -> LifeCycleStage:
    """
    Save a stage to the database.
    
    Args:
        stage: Stage data as a dictionary
        project_id: Optional project ID to associate with the stage
        
    Returns:
        The saved LifeCycleStage object
    """
    # Get database session
    db = get_db()
    
    try:
        # Create a new stage
        new_stage = LifeCycleStage(
            name=stage["name"],
            project_id=project_id
        )
        new_stage.activities_list = stage["activities"]
        
        # Add to database
        db.add(new_stage)
        db.commit()
        
        logger.info(f"Saved stage: {new_stage.name}")
        return new_stage
    except Exception as e:
        db.rollback()
        logger.error(f"Error saving stage: {e}")
        raise
    finally:
        db.close()