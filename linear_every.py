import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
TAKELAND_TIME = 2 #min

areaWidth = 500#ft
areaLength = 122 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 

waitTime = 0 #min

#>>>>>check if long/wide enough for this config

#if width is longer, this function returns "True"
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)
    
#find max gateToPadRatio
def maxGateToPadRatio(width, length):
    if findLongerSide(width, length) == True:
        maxGatesToPad = math.floor(width/GATE_SIDE)
    else:
        maxGatesToPad = math.floor(length/GATE_SIDE)
    return(maxGatesToPad)

#find how much wait time there would be
#based on assumption of gate time (6) & landTake time (2)
def calculateWaitTime(gateToPadRatio):
    waitTime = 0
    if gateToPadRatio == 2:
        #for every 2 trips, 2 minute wait time in gate
        waitTime += 2/2
    elif gateToPadRatio == 3:
        #for every 3 trips, 2 minutes is added
        waitTime += 2/3
    elif gateToPadRatio > 3:
        #add 4 minutes for every gate after the 3rd gate
        waitTime += (4 * (gateToPadRatio - 3)) + 2
    else:
        waitTime = 0
    return(waitTime)

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
def checkVertiports(width, length, gatesToPad):
    if findLongerSide(width, length) == True:
        totalGates = math.floor(width/GATE_SIDE)
        vertiports = math.floor(totalGates/gatesToPad)
        maxNumVertiports = math.floor(width/VERTIPORT_SIDE)
        #At some point the length of vertiports becomes greater than the length of gates
        if vertiports >= maxNumVertiports:
            vertiports = maxNumVertiports
        else:
            vertiports = vertiports
    else:
        totalGates = math.floor(length/GATE_SIDE)
        vertiports = math.floor(totalGates/gatesToPad)
        maxNumVertiports = math.floor(length/VERTIPORT_SIDE)

        if vertiports >= maxNumVertiports:
            vertiports = maxNumVertiports
        else:
            vertiports = vertiports
    return(vertiports)

#print out throughput (flights per hour) for every gateToPadRatio & list of gateToPadRatios and waitTimes
def calculateFlights(width, length, vertiports, gateToPadRatio):
    #>>>>>turn into dictionary with corresponding ratios eventually (aka a table with wait time, flights, ratio, vertiports)
    gateToPadRatioEvery = []
    vertiportsEvery = []
    numFlightsEvery = []
    waitTime = 0
    waitTimeEvery = []
    landTakeTime = 2
    cycleTime = landTakeTime + waitTime
    
    if checkMaybeDouble(width, length) == True:
        Double = 2
    else:
        Double = 1

    #greater than 1, because 1 gate would be pointless
    while gateToPadRatio > 1:
        gateToPadRatioEvery.append(gateToPadRatio)

        waitTime = calculateWaitTime(gateToPadRatio)
        waitTimeEvery.append(waitTime)

        vertiports = checkVertiports(width, length, gateToPadRatio) * Double
        vertiportsEvery.append(vertiports)

        cycleTime = landTakeTime + waitTime

        numFlights = (60/cycleTime) * (vertiports * gateToPadRatio)
        numFlightsEvery.append(numFlights)

        gateToPadRatio -= 1
    
    return(gateToPadRatioEvery, waitTimeEvery, vertiportsEvery, numFlightsEvery)

#find largest throughput & corresponding gateToPadRatio

#calculate number of vertiports for this gateToPadRatio



print(f"Area Width: {areaWidth}, Area Length: {areaLength}")
if findLongerSide(areaWidth, areaLength) == True:
    print("Longer Side: Width OR Same")
else:
    print("Longer Side: Length")

gatesToPad = maxGateToPadRatio(areaWidth, areaLength)
print("Maxium Gate To Pad Ratio: " + str(gatesToPad))

# waitTime = calculateWaitTime(gatesToPad)
# print("Wait Time for " + str(gatesToPad) + " Ratio: " + str(waitTime))

maybeDouble = checkMaybeDouble(areaWidth, areaLength)
print("Short Side Long Enough To Double: " + str(maybeDouble))

# vertiports = checkVertiports(areaWidth, areaLength, gatesToPad)
# print("Total # Vertiports: " + str(vertiports))

gatesToPad, waitTime, vertiports, numFlights = calculateFlights(areaWidth, areaLength, vertiports, gatesToPad)
print(f"Gate To Pad Ratios: {gatesToPad}")
print(f"Wait Times: {waitTime}")
print(f"Vertiports: {vertiports}")
print(f"Number of Flights Per Hour: {numFlights}")

