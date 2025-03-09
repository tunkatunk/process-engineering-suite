"""
Configuration settings for the Life Cycle Analysis (LCA) module.
"""

# Default impact factors for common activities
# Format: activity_name: (co2_kg, water_l, energy_kwh)
DEFAULT_IMPACT_FACTORS = {
    "electricity_generation_coal_kwh": (1.1, 2.0, 1.0),
    "electricity_generation_natural_gas_kwh": (0.5, 1.0, 1.0),
    "electricity_generation_solar_kwh": (0.05, 0.1, 1.0),
    "electricity_generation_wind_kwh": (0.02, 0.1, 1.0),
    "transportation_truck_km": (0.1, 0.02, 0.4),
    "transportation_ship_km": (0.01, 0.005, 0.1),
    "transportation_rail_km": (0.03, 0.01, 0.2),
    "material_steel_kg": (2.0, 50.0, 25.0),
    "material_aluminum_kg": (8.0, 100.0, 45.0),
    "material_plastic_kg": (3.0, 80.0, 30.0),
    "material_glass_kg": (0.8, 10.0, 15.0),
    "material_concrete_kg": (0.2, 1.0, 1.0),
    "material_paper_kg": (1.0, 30.0, 10.0),
    "waste_landfill_kg": (0.5, 0.1, 0.1),
    "waste_recycling_kg": (0.1, 5.0, 1.0),
    "waste_incineration_kg": (2.0, 0.5, -0.5)  # Negative energy means energy recovery
}

# LCA default settings
DEFAULT_SETTINGS = {
    "default_stages": ["Raw Material Extraction", "Manufacturing", "Transportation", "Use", "End of Life"],
    "chart_colors": ["#3366CC", "#DC3912", "#FF9900", "#109618", "#990099"],
    "export_formats": ["pdf", "csv", "xlsx"],
    "calculation_precision": 3,  # Decimal places
    "include_uncertainty": True  # Whether to include uncertainty in calculations
}

# LCA database settings
DATABASE = {
    "use_external_db": False,  # Set to True to use external LCA database
    "external_db_path": "",    # Path to external database (e.g., ecoinvent)
    "cache_external_data": True
}