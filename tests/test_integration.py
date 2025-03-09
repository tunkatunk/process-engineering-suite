"""
Integration tests for the application.
"""
import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.data.database import Base
from src.core.data.models import User, Project
from src.modules.lca.src.models import LifeCycleStage, ImpactFactor
from src.modules.lca.src.controllers import calculate_impact

@pytest.fixture
def db_session():
    """Create an in-memory database session for testing."""
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_lca_integration(db_session):
    """Test LCA functionality with the core database models."""
    # Create a user
    user = User(name="Test User", email="test@example.com", role="engineer")
    db_session.add(user)
    
    # Create a project
    project = Project(name="Test Project", description="Integration test project", owner=user)
    db_session.add(project)
    
    # Create impact factors
    impact_factors = [
        ImpactFactor(activity="material_steel_kg", co2=2.0, water=50.0, energy=25.0),
        ImpactFactor(activity="electricity_generation_coal_kwh", co2=1.1, water=2.0, energy=1.0)
    ]
    for factor in impact_factors:
        db_session.add(factor)
    
    # Commit to get IDs
    db_session.commit()
    
    # Create life cycle stages
    stages = [
        LifeCycleStage(
            name="Raw Materials",
            project=project,
            activities='[{"activity": "material_steel_kg", "quantity": 100}]'
        ),
        LifeCycleStage(
            name="Manufacturing",
            project=project,
            activities='[{"activity": "electricity_generation_coal_kwh", "quantity": 500}]'
        )
    ]
    for stage in stages:
        db_session.add(stage)
    
    db_session.commit()
    
    # Test loading stages from the database
    db_stages = db_session.query(LifeCycleStage).filter_by(project_id=project.id).all()
    assert len(db_stages) == 2
    
    # Calculate impact
    results = calculate_impact(db_stages)
    
    # Check results
    assert results["co2"] == 750.0
    assert results["water"] == 6000.0
    assert results["energy"] == 3000.0
    
    # Test project relationship
    assert db_stages[0].project.name == "Test Project"
    assert db_stages[0].project.owner.name == "Test User"