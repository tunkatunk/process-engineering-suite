"""
Data models for the LCA module.
"""
from typing import Dict, List, Optional, Any
import json

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from core.data.database import Base

class ImpactFactor(Base):
    """Environmental impact factors for activities."""
    __tablename__ = "lca_impact_factors"
    
    id = Column(Integer, primary_key=True)
    activity = Column(String, nullable=False, unique=True)
    co2 = Column(Float, nullable=False)  # CO2 emissions in kg
    water = Column(Float, nullable=False)  # Water usage in L
    energy = Column(Float, nullable=False)  # Energy use in kWh
    
    def __repr__(self) -> str:
        return f"<ImpactFactor {self.activity}>"
    
    @property
    def as_dict(self) -> Dict[str, Any]:
        """Return the impact factor as a dictionary."""
        return {
            "id": self.id,
            "activity": self.activity,
            "co2": self.co2,
            "water": self.water,
            "energy": self.energy
        }

class LifeCycleStage(Base):
    """A stage in a product or process life cycle."""
    __tablename__ = "lca_stages"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    activities = Column(String)  # JSON string of activities and quantities
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # Relationships
    project = relationship("Project")
    
    def __repr__(self) -> str:
        return f"<LifeCycleStage {self.name}>"
    
    @property
    def activities_list(self) -> List[Dict[str, Any]]:
        """
        Get the activities as a list of dictionaries.
        
        Returns:
            List of dictionaries with keys 'activity' and 'quantity'
        """
        if self.activities:
            return json.loads(self.activities)
        return []
    
    @activities_list.setter
    def activities_list(self, activities: List[Dict[str, Any]]) -> None:
        """
        Set the activities from a list of dictionaries.
        
        Args:
            activities: List of dictionaries with keys 'activity' and 'quantity'
        """
        self.activities = json.dumps(activities)
    
    @property
    def as_dict(self) -> Dict[str, Any]:
        """Return the stage as a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "activities": self.activities_list,
            "project_id": self.project_id
        }