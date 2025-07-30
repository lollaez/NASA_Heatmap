import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
SAFETY_SIDE = 48
TAXIWAY_SIDE = 48 * 1.5
TAKELAND_TIME = 2 #min
CYCLE_TIME = TAKELAND_TIME #min

areaWidth = 607 #ft
areaLength = 570 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 

def check_area_triple2(width, length):
    safety_needed = False
    large_enough = False
    if width >= (VERTIPORT_SIDE + TAXIWAY_SIDE) and length >= (VERTIPORT_SIDE + TAXIWAY_SIDE):
        #4 gates are needed for this configuration to make sense
        if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4) or length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
            print("Large Enough With Safety Area")
            safety_needed = False
            large_enough = True
        elif (width + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4) or (length + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
            print("Large Enough Without Safety Area - Gate Side Too Short")
            safety_needed = True
            large_enough = True
    elif (width + SAFETY_SIDE) >= (VERTIPORT_SIDE + TAXIWAY_SIDE) and (length + SAFETY_SIDE) >= (VERTIPORT_SIDE + TAXIWAY_SIDE):
        if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4) or length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
            print("Large Enough Without Safety Area - Pad Side Too Short")
            safety_needed = True
            large_enough = True
        elif (width + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4) or (length + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
            print("Large Enough Without Safety Area - Both Too Short")
            safety_needed = True
            large_enough = True
    else:
        safety_needed = False
        large_enough = False
    return(large_enough, safety_needed)
    
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)

def calcVertiportsTriple2(width, length):
    large_enough, safety_needed = check_area_triple2(areaWidth, areaLength)
    long_enough = True
    
    if safety_needed == False:
        #need to double check that the shorter side is long enough for 4 gates & 2pads
        if findLongerSide(width, length) == True:
            if length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
                long_enough = True
            else:
                long_enough = False
        else:
            if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
                long_enough = True
            else:
                long_enough = False

        if long_enough == True:
            if findLongerSide(width, length) == True:
                vertiports = math.floor(width/(VERTIPORT_SIDE + TAXIWAY_SIDE))
                vertiports_safety = math.floor((width + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
            else:
                vertiports = math.floor(length/(VERTIPORT_SIDE + TAXIWAY_SIDE))
                vertiports_safety = math.floor((length + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
        else:
            if findLongerSide(width, length) == True:
                vertiports = math.floor(length/(VERTIPORT_SIDE + TAXIWAY_SIDE))
                vertiports_safety = math.floor((length + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
            else:
                vertiports = math.floor(width/(VERTIPORT_SIDE + TAXIWAY_SIDE))
                vertiports_safety = math.floor((width + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    else:
        if findLongerSide(width, length) == True:
            #need to double check that the shorter side is long enough for 4 gates & 2pads
            if (length + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
                long_enough = True
            else:
                long_enough = False

            #depending on that info, caculate # of vertiports based on shorter or longer sided
            if long_enough == True:
                vertiports = 0
                vertiports_safety = math.floor((width + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
            else:
                vertiports = 0
                vertiports_safety = math.floor((length + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
        else:
            #need to double check that the shorter side is long enough for 4 gates & 2pads
            if (width + SAFETY_SIDE) >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
                long_enough = True
            else:
                long_enough = False

            #depending on that info, caculate # of vertiports based on shorter or longer sided
            if long_enough == True:
                vertiports = 0
                vertiports_safety = math.floor((length + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))
            else:
                vertiports = 0
                vertiports_safety = math.floor((width + SAFETY_SIDE)/(VERTIPORT_SIDE + TAXIWAY_SIDE))

    return(vertiports, vertiports_safety)

def calculate_flights_triple2(vertiports):    
    numFlights = (60/CYCLE_TIME) * (vertiports)
    return(numFlights)

print(f"Area Width: {areaWidth}, Area Length: {areaLength}")

if findLongerSide(areaWidth, areaLength) == True:
    print("Longer Side: Width OR Same")
else:
    print("Longer Side: Length")

large_enough, safety_needed = check_area_triple2(areaWidth, areaLength)
if large_enough == True:
    vertiports, vertiports_safety = calcVertiportsTriple2(areaWidth, areaLength)
    numFlights = calculate_flights_triple2(vertiports)
    numFlightsSafety = calculate_flights_triple2(vertiports_safety)

    print(f"Vertiports for Triple 2.0: {vertiports}")
    print(f"Flights per Hour for Triple 2.0: {numFlights}")
    
    print(f"(Without Safety) Vertiports for Triple 2.0: {vertiports_safety}")
    print(f"(Without Safety) Flights per Hour for Triple 2.0: {numFlightsSafety}")

else:
    print("Area Not Large Enough for Triple 2.0")