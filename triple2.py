import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
SAFETY_SIDE = 48
TAXIWAY_SIDE = 48 * 1.5
TAKELAND_TIME = 2 #min
CYCLE_TIME = TAKELAND_TIME #min

areaWidth = 517 #ft
areaLength = 600 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 

def check_area_triple2(width, length):
    if width >= (VERTIPORT_SIDE + TAXIWAY_SIDE) and length >= (VERTIPORT_SIDE + TAXIWAY_SIDE):
        #4 gates are needed for this configuration to make sense
        if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4) or length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 4):
            return(True)
        else:
            return(False)
    else:
        return(False)
    
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)

def calcVertiportsTriple2(width, length):
    if findLongerSide(width, length) == True:
        vertiports = math.floor(width/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    else:
        vertiports = math.floor(length/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    return(vertiports)

def calculate_flights_triple2(vertiports):    
    numFlights = (60/CYCLE_TIME) * (vertiports)
    return(numFlights)

print(f"Area Width: {areaWidth}, Area Length: {areaLength}")
if findLongerSide(areaWidth, areaLength) == True:
    print("Longer Side: Width OR Same")
else:
    print("Longer Side: Length")

if check_area_triple2(areaWidth, areaLength) == True:
    vertiportsVert = calcVertiportsTriple2(areaWidth, areaLength)
    print(f"Vertiports for Triple 2.0: {vertiportsVert}")
    
    numFlightsVert = calculate_flights_triple2(vertiportsVert)
    print(f"Flights per Hour for Triple 2.0: {numFlightsVert}")

else:
    print("Area Not Large Enough for Triple 2.0")