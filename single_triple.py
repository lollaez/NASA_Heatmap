import math

#change to be able to import table of places & export same table but with data on different configurations
#output a graph of different configurations and their throughput - build upon other research paper
#determines which topology is best for a space depending on - size, width/length ratio,
#Include different configurations
#Include travel time between different parts

area_width = 436 #ft
area_length = 617 #ft
flight_time = 10 #min
#2 gates, one gate no wait time, second gate 4 mins due to sitting in gate
flight_time_triple = 2 + 4/2 #min

#drop-off/pick-up can be smaller because it does not need the safety area (Double check w/research)
VERTIPORT_SIDE = 144 #ft
GATE_SIDE = 72
#area = area_length * area_width

#checking that the given area is big enough for a vertiport
def check_area_single(width, length):
    if width >= VERTIPORT_SIDE and length >= VERTIPORT_SIDE:
        return(True)
    else:
        return(False)

#width needs to be longer 
def check_area_triple(width, length):
    if width >= VERTIPORT_SIDE and length >= VERTIPORT_SIDE:
        if width >= ((VERTIPORT_SIDE * 2) + GATE_SIDE) or length >= width >= ((VERTIPORT_SIDE * 2) + GATE_SIDE):
            return(True)
        else:
            return(False)
    else:
        return(False)

#checks if short side is long enough to double, can only double because it wouldn't make sense otherwise
def double_single(width, length):
    if width >= length:
        if width >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)
    else:
        if length >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)

#calculate number of vertiports with one area for landing, dropoff, & takeoff
def calculate_vertiports_single(width, length):
    #find the longer side
    if width >= length:
    #Make ony 100 x 100 ft boxes of vertiports and not include excess areas
        number_width = math.floor(width/VERTIPORT_SIDE)
        #double?
        if double_single(width, length) == True:
            number_vertiports = number_width * 2
        else:
            number_vertiports = number_width
    else:
        number_length = math.floor(length/VERTIPORT_SIDE)
        if double_single(width, length) == True:
            number_vertiports = number_length * 2
        else:
            number_vertiports = number_length
    return(number_vertiports)
    
#calculate number of vertiports with different area for landing, dropoff, & takeoff
def calculate_vertiports_triple(width, length):
    #find the longer side
    if width >= length:
    #Make ony 100 x 110 ft boxes of vertiports and not include excess areas
        number_vertiports = math.floor(width/VERTIPORT_SIDE)
    else:
        number_vertiports = math.floor(length/VERTIPORT_SIDE)
    return(number_vertiports)
    
#calculates flights per hour based on minutes per flight
def calculate_flights(vertiports, time):
    flights = 60/time * vertiports
    return(flights)

print(f"Area Width: {area_width}, Area Length: {area_length}")

if check_area_single(area_width, area_length) == True:
    vertiports = calculate_vertiports_single(area_width, area_length)
    flights_single = calculate_flights(vertiports, flight_time)
    
    print( "Number of Vertiports (Single Config): " + str(vertiports))
    print("Number of Flights Per Hour (Single Config): " + str(flights_single))

if check_area_triple(area_width, area_length) == True:

    vertiports_triple = calculate_vertiports_triple(area_width, area_length)
    flights_triple = calculate_flights(vertiports_triple, flight_time_triple)

    print( "Number of Vertiports (Triple Config): " + str(vertiports_triple))
    print("Number of Flights Per Hour (Triple Config): " + str(flights_triple))
