import math

VERTIPORT_SIDE = 144 #ft archer midnight
SAFTEY_SIDE = 25 #ft
GATE_SIDE = 55 #ft wingspan 48ft <- change to larger porportion
TAKELAND_TIME = 2 #min
ATGATE_TIME = 5 #min

areaWidth = 500 #ft
areaLength = 1000 #ft

numGates = 0
numPaths = 0

toGateTime = 0 #min
toTakeTime = 0 #min
travelTime = 0 #min toGateTime + toTakeTime
taxiwayLength = 0 #ft 
numFlights = 0 #flights per hour 
extraFlights = 0 #flights other than the first one that can happen in one hour
totalTime = 0 #min 
waitTime = 0 #min
totalLength = VERTIPORT_SIDE * 2 + taxiwayLength - SAFTEY_SIDE * 2 #ft
#signals eVTOL has taken off
cycleComplete = False
locationEVTOL = "Sky"

#if width is longer, this function returns "True"
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)

#don't need because total length is the side length of the area...
# def calculateLength():

def calculateGate(width, length):
    if findLongerSide(width, length) ==True:
        numGates = math.floor((width - (VERTIPORT_SIDE - SAFTEY_SIDE) * 2)/GATE_SIDE)
        return(numGates)
    else:
        numGates = math.floor((length - (VERTIPORT_SIDE - SAFTEY_SIDE) * 2)/GATE_SIDE)
        return(numGates)

#time per cycle of eVTOL passing through station
def calculateTime(width, length):
    numGates = calculateGate(width, length)
    travelTime = numGates + 1
    totalTime = TAKELAND_TIME * 2 + travelTime + ATGATE_TIME 
    return(totalTime)

def calculateFlights(width, length):
    flights = 60/time * vertiports
    return(flights)
    #The other airtaxi will always only be 2 mins behind
    # totalTime = calculateTime(width, length)
    # multiFlightTime = 0
    # extraFlights = 0
    # while multiFlightTime != 60:
    #     #edit to account for wait time, if there is any
    #     multiFlightTime = totalTime + 2 * extraFlights
    #     if (multiFlightTime + 2) >= 60:
    #         return (extraFlights)
    #     else:
    #       extraFlights += 1  

if findLongerSide(areaWidth, areaLength) == True:
    print("Width Longer OR Same")
else:
    print("Length Longer")

print(calculateGate(areaWidth, areaLength))
print(calculateTime(areaWidth, areaLength))

extraFlights = calculateFlights(areaWidth, areaLength)
print("Max Num of Extra Flights: " + str(extraFlights))

numFlights = calculateFlights(areaWidth, areaLength) + 1
print("Flights Per Hour: " + str(numFlights))
    

