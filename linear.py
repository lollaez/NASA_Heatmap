import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
TAKELAND_TIME = 2 #min

areaWidth = 517 #ft
areaLength = 600 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 
cycleTime = 0 #min

#>>>>>check if long/wide enough for this config
def check_area_linear(width, length):
    if width >= (VERTIPORT_SIDE + GATE_SIDE) and length >= (VERTIPORT_SIDE + GATE_SIDE):
        return(True)
    else:
        return(False)

#if width is longer, this function returns "True"
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)

#Check if short side long enough to double
def checkMaybeDouble(width, length):
    if findLongerSide(width, length) == True:
        if length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
            return(True)
        else:
            return(False)
    else:
        if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
            return(True)
        else:
            return(False)

#find number of vertiports based on gateToPadRatio
def checkVertiportsLinear(width, length):
    if findLongerSide(width, length) == True:
        totalGates = math.floor(width/GATE_SIDE)
        vertiports3 = math.floor(totalGates/3)
        vertiports2 = math.floor(totalGates/2)
    else:
        totalGates = math.floor(length/GATE_SIDE)
        vertiports3 = math.floor(totalGates/3)
        vertiports2 = math.floor(totalGates/2)
    return(vertiports3, vertiports2)

#print out throughput (flights per hour) for every gateToPadRatio & list of gateToPadRatios and waitTimes
def calculateFlights(width, length, vertiports, cycleTime):
    #>>>>>turn into dictionary with corresponding ratios eventually (aka a table with wait time, flights, ratio, vertiports)
    if checkMaybeDouble(width, length) == True:
        Double = 2
    else:
        Double = 1

    numFlights = (60/cycleTime) * (vertiports) * Double
    return(numFlights)

#find largest throughput & corresponding gateToPadRatio

#calculate number of vertiports for this gateToPadRatio



print(f"Area Width: {areaWidth}, Area Length: {areaLength}")
if findLongerSide(areaWidth, areaLength) == True:
    print("Longer Side: Width OR Same")
else:
    print("Longer Side: Length")

if check_area_linear(areaWidth, areaLength) == True:
    maybeDouble = checkMaybeDouble(areaWidth, areaLength)
    print("Short Side Long Enough To Double: " + str(maybeDouble))

    vertiports3, vertiports2 = checkVertiportsLinear(areaWidth, areaLength)
    print(f"Vertiports With Ratio 3: {vertiports3}, Vertiports With Ratio 2: {vertiports2}")

    numFlightsLinear3 = calculateFlights(areaWidth, areaLength, vertiports3, 4.66)
    numFlightsLinear2 = calculateFlights(areaWidth, areaLength, vertiports2, 5)
    print(f"Flights With Ratio 3: {numFlightsLinear3} Flights With Ratio 2: {numFlightsLinear2}")
    
else:
    print("Area Not Large Enough for Linear")

