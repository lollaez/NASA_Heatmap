import math

VERTIPORT_SIDE = 144 #ft archer midnight
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 55 #ft wingspan 48ft <- change to larger porportion
TAKELAND_TIME = 2 #min
#to make it easier for myself make it a multiple of 2
ATGATE_TIME = 6 #min

areaWidth = 500 #ft
areaLength = 1000 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 

landTakeTime = 2 #min
gateTime = 5 #min
waitTime = 0 #min

#check if long/wide enough for this config

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
    if gateToPadRatio > 3:
        #adds 2 minute for every extra gate
        waitTime += 2 * (gateToPadRatio - 3)
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
        vertiports = totalGates/gatesToPad
    else:
        totalGates = math.floor(length/GATE_SIDE)
        vertiports = totalGates/gatesToPad
    return(vertiports)

#print out throughput (flights per hour) for a gateToPadRatio
def calculateFlights(width, length, vertiports, gateToPadRatio):
    cycleTime = landTakeTime + waitTime
    if checkMaybeDouble(width, length) == True:
        numFlights = (60/cycleTime) * (vertiports * gateToPadRatio) * 2
    else:
        numFlights = 60/(cycleTime * vertiports * gateToPadRatio)
    return(numFlights)



if findLongerSide(areaWidth, areaLength) == True:
    print("Width Longer OR Same")
else:
    print("Length Longer")

gatesToPad = maxGateToPadRatio(areaWidth, areaLength)
print("Maxium Gate To Pad Ratio: " + str(gatesToPad))

waitTime = calculateWaitTime(gatesToPad)
print("Wait Time for " + str(gatesToPad) + " Ratio: " + str(waitTime))

maybeDouble = checkMaybeDouble(areaWidth, areaLength)
print("Short Side Long Enough To Double: " + str(maybeDouble))

vertiports = checkVertiports(areaWidth, areaLength, gatesToPad)
print("Total # Vertiports: " + str(vertiports))

numFlights = calculateFlights(areaWidth, areaLength, vertiports, gatesToPad)
print("Flights Per Hour: " + str(numFlights))

