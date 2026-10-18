def parse_telemetry(raw_data):
    """
    Simulates parsing UGV telemetry packets.
    Expected format: "SPEED:45,VOLT:24.2"
    """
    try:
        parts = raw_data.split(",")
        speed = float(parts[0].split(":")[1])
        voltage = float(parts[1].split(":")[1])
        return speed, voltage
    except (IndexError, ValueError):
        raise ValueError("Invalid telemetry packet format!")