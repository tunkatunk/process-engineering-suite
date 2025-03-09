"""
Tests for the LCA module models.
"""
import json
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.modules.lca.src.models import LifeCycleStage, ImpactFactor
from core.data.database import Base

@pytest.fixture
def db_session():
    """Create an in-memory database session for testing."""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_impact_factor_creation(db_session):
    """Test creating an impact factor."""
    # Create an impact factor
    impact_factor = ImpactFactor(
        activity="electricity_generation_coal_kwh",
        co2=1.1,
        water=2.0,
        energy=1.0
    )
    
    # Add to database
    db_session.add(impact_factor)
    db_session.commit()
    
    # Retrieve from database
    retrieved = db_session.query(ImpactFactor).first()
    
    # Check values
    assert retrieved.activity == "electricity_generation_coal_kwh"
    assert retrieved.co2 == 1.1
    assert retrieved.water == 2.0
    assert retrieved.energy == 1.0
    assert retrieved.as_dict == {
        "id": retrieved.id,
        "activity": "electricity_generation_coal_kwh",
        "co2": 1.1,
        "water": 2.0,
        "energy": 1.0
    }

def test_life_cycle_stage_creation(db_session):
    """Test creating a life cycle stage."""
    # Create activities
    activities = [
        {"activity": "electricity_generation_coal_kwh", "quantity": 100},
        {"activity": "transportation_truck_km", "quantity": 500}
    ]
    
    # Create a stage
    stage = LifeCycleStage(
        name="Manufacturing",
        activities=json.dumps(activities)
    )
    
    # Add to database
    db_session.add(stage)
    db_session.commit()
    
    # Retrieve from database
    retrieved = db_session.query(LifeCycleStage).first()
    
    # Check values
    assert retrieved.name == "Manufacturing"
    assert retrieved.activities_list == activities
    
    # Test setting activities_list
    new_activities = [
        {"activity": "material_steel_kg", "quantity": 200}
    ]
    retrieved.activities_list = new_activities
    db_session.commit()
    
    # Retrieve again
    updated = db_session.query(LifeCycleStage).first()
    assert updated.activities_list == new_activities
    
    # Check as_dict
    assert updated.as_dict == {
        "id": updated.id,
        "name": "Manufacturing",
        "activities": new_activities,
        "project_id": None
    }