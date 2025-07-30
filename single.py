import math

area_width = 121 #ft
area_length = 502 #ft

flight_time = 10 #min

#drop-off/pick-up can be smaller because it does not need the safety area (Double check w/research)
VERTIPORT_SIDE = 144 #ft
SAFETY_SIDE = 48 #ft
GATE_SIDE = 72
#area = area_length * area_width

#checking that the given area is big enough for a vertiport
def check_area_single(width, length):
    safety_needed = False
    large_enough = False
    if width >= VERTIPORT_SIDE and length >= VERTIPORT_SIDE:
        print("Large Enough With Safety Area")
        safety_needed = False
        large_enough = True
    elif width >= (VERTIPORT_SIDE - SAFETY_SIDE) and length >= (VERTIPORT_SIDE - SAFETY_SIDE):
        print("Large Enough Without Safety Area")
        if width < VERTIPORT_SIDE:
            print("Width Is Too Short If Safety Area Needed")
            safety_needed = True
            large_enough = True
        else:
            print("Length Is Too Short If Safety Area Needed")
            safety_needed = True
            large_enough = True
    else:
        safety_needed = False
        large_enough = False
    return(large_enough, safety_needed)

#checks if short side is long enough to double, can only double because it wouldn't make sense otherwise
def double_single(width, length):
    if width >= length:
        if length >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)
    else:
        if width >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)
        
def double_single_safety(width, length):
    if width >= length:
        if (length + SAFETY_SIDE) >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)
    else:
        if (width + SAFETY_SIDE) >= 2 * VERTIPORT_SIDE:
            return(True)
        else:
            return(False)

#calculate number of vertiports with one area for landing, dropoff, & takeoff
def calculate_vertiports_single(width, length):
    #find the longer side
    if double_single(width, length) == True:
        print("Long Enough To Double")
        double = 2    
    else:
        double = 1
    
    if double_single_safety(width, length) == True:
        print("Long Enough To Double Without Safety")
        doubleSafety = 2    
    else:
        doubleSafety = 1

    large_enough, safety_needed = check_area_single(area_width, area_length)

    if width >= length:
        if safety_needed == False:
            number_width = math.floor(width/VERTIPORT_SIDE)
            number_vertiports = number_width * double
            number_width_safety = math.floor((width + SAFETY_SIDE)/VERTIPORT_SIDE)
            number_vertiports_safety = number_width_safety * doubleSafety
        else:
            number_vertiports = 0
            number_width_safety = math.floor((width + SAFETY_SIDE)/VERTIPORT_SIDE)
            number_vertiports_safety = number_width_safety * doubleSafety
    else:
        if safety_needed == False:
            number_length = math.floor(length/VERTIPORT_SIDE)
            number_vertiports = number_length * double
            number_length_safety = math.floor((length + SAFETY_SIDE)/VERTIPORT_SIDE)
            number_vertiports_safety = number_length_safety * doubleSafety

        else:
            number_vertiports = 0
            number_length_safety = math.floor((length + SAFETY_SIDE)/VERTIPORT_SIDE)
            number_vertiports_safety = number_length_safety * doubleSafety

    return(number_vertiports, number_vertiports_safety)
    
#calculates flights per hour based on minutes per flight
def calculate_flights(vertiports, time):
    flights = 60/time * vertiports
    return(flights)

print(f"Area Width: {area_width}, Area Length: {area_length}")
large_enough, safety_needed = check_area_single(area_width, area_length)

if large_enough == True:
    vertiports, vertiports_safety = calculate_vertiports_single(area_width, area_length)
    flights_single = calculate_flights(vertiports, flight_time)
    flights_single_safety = calculate_flights(vertiports_safety, flight_time)
    
    print( "Number of Vertiports (Single Config): " + str(vertiports))
    print("Flights Per Hour (Single Config): " + str(flights_single))
    print( "(Without Safety) Number of Vertiports (Single Config): " + str(vertiports_safety))
    print("(Without Safety) Flights Per Hour (Single Config): " + str(flights_single_safety))
else:
    print("Area Not Large Enough For Single")
