import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
TAXIWAY_SIDE = 48 * 1.5
TAKELAND_TIME = 2 #min

areaWidth = 1000#ft
areaLength = 500 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 

waitTime = 0 #min

def check_area_triple2(width, length):
    if width >= (VERTIPORT_SIDE + TAXIWAY_SIDE) and length >= (VERTIPORT_SIDE + TAXIWAY_SIDE):
        #2 gates is the least to make it make sense
        if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2) or length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
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

#Horizontal longer side to ind gateToPadRatio
def gateToPadRatioHoriz(width, length):
    if findLongerSide(width, length) == True:
        GatesToPad = math.floor((width - (VERTIPORT_SIDE * 2))/GATE_SIDE)
    else:
        GatesToPad = math.floor((length - (VERTIPORT_SIDE * 2))/GATE_SIDE)
    return(GatesToPad)

def calcVertiportsHoriz(width, length):
    if findLongerSide(width, length) == True:
        vertiports = math.floor(length/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    else:
        vertiports = math.floor(width/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    return(vertiports)

#Vertical longer side to find # of vertiports
def calcVertiportsVert(width, length):
    if findLongerSide(width, length) == True:
        vertiports = math.floor(width/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    else:
        vertiports = math.floor(length/(VERTIPORT_SIDE + TAXIWAY_SIDE))
    return(vertiports)
    
def gateToPadRatioVert(width, length):
    if findLongerSide(width, length) == True:
        GatesToPad = math.floor((length - (VERTIPORT_SIDE * 2))/GATE_SIDE)
    else:
        GatesToPad = math.floor((width - (VERTIPORT_SIDE * 2))/GATE_SIDE)
    return(GatesToPad)

def calculateWaitTime(gateToPadRatio):
    #not taking into account travel time along taxiway
    waitTime = 0
    if gateToPadRatio == 2:
        #for every 2 trips, 2 minute wait time in gate
        waitTime += 2/2
    elif gateToPadRatio == 3:
        #for every 3 trips, 2 minutes is added
        waitTime += 2/3
    elif gateToPadRatio == 4:
        waitTime = 0
    elif gateToPadRatio > 3:
        #add 4 minutes for every gate after the 3rd gate
        waitTime += (2 * (gateToPadRatio - 4))
    else:
        waitTime = 0
    return(waitTime)

def calculate_flights_triple2(vertiports, gatesToPad, waitTime):    
    cycleTime = TAKELAND_TIME + waitTime
    numFlights = (60/cycleTime) * (vertiports * gatesToPad)
    return(numFlights)

print(f"Area Width: {areaWidth}, Area Length: {areaLength}")
if findLongerSide(areaWidth, areaLength) == True:
    print("Longer Side: Width OR Same")
else:
    print("Longer Side: Length")

if check_area_triple2(areaWidth, areaLength) == True:
    gatesToPadHoriz = gateToPadRatioHoriz(areaWidth, areaLength)
    print(f"Gate To Pad Ratio for Triple 2.0 Horiz: {gatesToPadHoriz}")
    vertiportsHoriz = calcVertiportsHoriz(areaWidth, areaLength)
    print(f"Vertiports for Triple 2.0 Horiz: {vertiportsHoriz}")
    waitTimeHoriz = calculateWaitTime(gatesToPadHoriz)
    print(f"Wait Time for Triple 2.0 Horiz: {waitTimeHoriz}")
    numFlightsHoriz = calculate_flights_triple2(vertiportsHoriz, gatesToPadHoriz, waitTimeHoriz)
    print(f"Flights per Hour for Triple 2.0 Horiz: {numFlightsHoriz}")

    print("-----------------------------------------------------")

    gatesToPadVert = gateToPadRatioVert(areaWidth, areaLength)
    print(f"Gate To Pad Ratio for Triple 2.0 Vert: {gatesToPadVert}")
    vertiportsVert = calcVertiportsVert(areaWidth, areaLength)
    print(f"Vertiports for Triple 2.0 Vert: {vertiportsVert}")
    waitTimeVert = calculateWaitTime(gatesToPadVert)
    print(f"Wait Time for Triple 2.0 Vert: {waitTimeVert}")
    numFlightsVert = calculate_flights_triple2(vertiportsVert, gatesToPadVert, waitTimeVert)
    print(f"Flights per Hour for Triple 2.0 Vert: {numFlightsVert}")