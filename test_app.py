import pytest
from app import parse_telemetry

def test_parse_telemetry_normal():
    # Test valid telemetry data
    speed, voltage = parse_telemetry("SPEED:30,VOLT:23.5")
    assert speed == 30.0
    assert voltage == 23.5

def test_parse_telemetry_safety_limit():
    # Test that speed doesn't exceed safe bounds (e.g., max 60)
    speed, voltage = parse_telemetry("SPEED:55,VOLT:22.0")
    assert speed <= 60.0, "Safety Warning: UGV speed exceeds safe operating threshold!"

def test_parse_telemetry_invalid():
    # Test error handling for malformed data
    with pytest.raises(ValueError):
        parse_telemetry("INVALID_DATA")