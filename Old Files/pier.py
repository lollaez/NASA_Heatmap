import math

def calculate_vertiports_and_flights(area_total, area_per_vertiport, gates_per_vertiport=4, fatos_per_vertiport=1, taxiways_per_vertiport=1, cycle_time=10, landing_time=2, takeoff_time=2, wait_time=6, gates_per_fato=4):
    # Calculate number of vertiports that fit in the total area
    vertiports = math.floor(area_total / area_per_vertiport)  # Using math.floor explicitly to round down
    
    # Total time per flight cycle (landing + takeoff + waiting at the gate)
    flight_cycle_time = landing_time + takeoff_time + wait_time  # Total 10 minutes per flight cycle
    
    # Flights per hour per gate (assuming no other limits)
    flights_per_gate_per_hour = 60 // flight_cycle_time  # How many flights can one gate handle per hour
    
    # The limiting factor will be the lower of:
    # - Flights per gate (gates_per_vertiport * flights per gate)
    # - Flights per FATO (fatos_per_vertiport * flights per FATO)
    flights_per_hour_per_vertiport = min(flights_per_gate_per_hour * gates_per_vertiport, fatos_per_vertiport * (60 // flight_cycle_time))
    
    # Total flights per hour across all vertiports
    total_flights_per_hour = flights_per_hour_per_vertiport * vertiports
    
    # Ratios and final breakdown
    flights_per_vertiport_ratio = flights_per_hour_per_vertiport / total_flights_per_hour if total_flights_per_hour > 0 else 0
    gates_per_vertiport_ratio = gates_per_vertiport  # Since each vertiport has 4 gates, it's a fixed ratio
    fatos_per_vertiport_ratio = fatos_per_vertiport 
    taxiways_per_vertiport_ratio = taxiways_per_vertiport

# Returning detailed outputs
    return {
        'Number of vertiports': vertiports,
        'Total flights per hour': total_flights_per_hour,
        'Flights per vertiport per hour': flights_per_hour_per_vertiport,
        'Flights per vertiport ratio': flights_per_vertiport_ratio,
        'Gates per vertiport': gates_per_vertiport,
        'FATOs per vertiport': fatos_per_vertiport,
        'Taxiways per vertiport': taxiways_per_vertiport,
        'Gates per vertiport ratio': gates_per_vertiport_ratio,
        'FATOs per vertiport ratio': fatos_per_vertiport_ratio,
        'Taxiways per vertiport ratio': taxiways_per_vertiport_ratio,
    }

# Example usage:
area_total = 1000000  # Example total area in square units
area_per_vertiport = 62208  # Area per vertiport

result = calculate_vertiports_and_flights(area_total, area_per_vertiport)

# Print detailed results
for key, value in result.items():
    print(f"{key}: {value}")
