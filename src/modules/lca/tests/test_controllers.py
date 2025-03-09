"""
Tests for the LCA module controllers.
"""
import os
import pytest
import pandas as pd
import tempfile

from src.modules.lca.src.controllers import calculate_impact, export_results

def test_calculate_impact():
    """Test the calculate_impact function."""
    # Create test stages
    stages = [
        {
            "name": "Raw Materials",
            "activities": [
                {"activity": "material_steel_kg", "quantity": 100}
            ]
        },
        {
            "name": "Manufacturing",
            "activities": [
                {"activity": "electricity_generation_coal_kwh", "quantity": 500}
            ]
        }
    ]
    
    # Calculate impact
    results = calculate_impact(stages)
    
    # Check results
    assert "co2" in results
    assert "water" in results
    assert "energy" in results
    
    # Check that results are positive numbers
    assert results["co2"] > 0
    assert results["water"] > 0
    assert results["energy"] > 0
    
    # Raw Materials: 100 kg steel
    # From DEFAULT_IMPACT_FACTORS: material_steel_kg = (2.0, 50.0, 25.0)
    # Manufacturing: 500 kWh coal electricity
    # From DEFAULT_IMPACT_FACTORS: electricity_generation_coal_kwh = (1.1, 2.0, 1.0)
    
    # Expected values:
    # co2 = 100 * 2.0 + 500 * 1.1 = 200 + 550 = 750
    # water = 100 * 50.0 + 500 * 2.0 = 5000 + 1000 = 6000
    # energy = 100 * 25.0 + 500 * 1.0 = 2500 + 500 = 3000
    
    assert results["co2"] == 750
    assert results["water"] == 6000
    assert results["energy"] == 3000

def test_export_results():
    """Test the export_results function."""
    # Create test data
    data = [
        ["Raw Materials", "200.00", "5000.00", "2500.00"],
        ["Manufacturing", "550.00", "1000.00", "500.00"],
        ["Total", "750.00", "6000.00", "3000.00"]
    ]
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Export results
        export_results(data, "csv", temp_path)
        
        # Check that file was created
        assert os.path.exists(temp_path)
        
        # Read the file and check contents
        df = pd.read_csv(temp_path)
        
        assert list(df.columns) == ["Stage", "CO2 (kg)", "Water (L)", "Energy (kWh)"]
        assert len(df) == 3
        assert df.iloc[0]["Stage"] == "Raw Materials"
        assert df.iloc[1]["Stage"] == "Manufacturing"
        assert df.iloc[2]["Stage"] == "Total"
        
        assert float(df.iloc[2]["CO2 (kg)"]) == 750.00
        assert float(df.iloc[2]["Water (L)"]) == 6000.00
        assert float(df.iloc[2]["Energy (kWh)"]) == 3000.00
    finally:
        # Clean up
        if os.path.exists(temp_path):
            os.unlink(temp_path)