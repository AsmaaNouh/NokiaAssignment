"""
FMT parser.

Assumed format example:

timestamp,lat,lng,value,route_id

Example:
16892312,30.123,31.456,-85,route_1
"""

def parse_line(line):

    parts = line.strip().split(",")

    # Skip malformed lines
    if len(parts) < 5:
        return None

    measurement = {

        "timestamp": int(parts[0]),

        "lat": float(parts[1]),

        "lng": float(parts[2]),

        "value": parts[3],

        "route_id": parts[4]

    }

    return measurement