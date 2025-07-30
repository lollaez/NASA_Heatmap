import math

VERTIPORT_SIDE = 48 * 3 #ft archer midnight - safety area = 3 times wingspan
#SAFTEY_SIDE = 25 #ft <- include in the future
GATE_SIDE = 48 * 1.5 #ft wingspan 48ft <- change to larger porportion (just driving)
TAKELAND_TIME = 2 #min
SAFETY_SIDE = 48

areaWidth = 718 #ft
areaLength = 183 #ft

gatesToPad = 0 #ratio of pads to each gate
maybeDouble = False #double # of vertiports & gates
totalGates = 0 #check total # of vertiports
vertiports = 0
numFlights = 0 #flights per hour 
cycleTime = 0 #min

def check_area_linear(width, length):
    #safety needed means if needs extra area to fit
    safety_needed = False
    large_enough = False
    max_gate_ratio = 0
    #check for both gate ratios
    if width >= (VERTIPORT_SIDE + GATE_SIDE) and length >= (VERTIPORT_SIDE + GATE_SIDE):
        print("Large Enough With Safety Area & Gate Ratio of 3")
        safety_needed = False
        large_enough = True
        large_enough = True
        max_gate_ratio = 3
    elif width >= (VERTIPORT_SIDE + GATE_SIDE) or length >= (VERTIPORT_SIDE + GATE_SIDE):
        if width >= VERTIPORT_SIDE and length >= VERTIPORT_SIDE:
            print("Large Enough With Safety Area & Gate Ratio of 2")
            safety_needed = False
            large_enough = True
            max_gate_ratio = 2
    #check if large enough without safety
    elif (width + SAFETY_SIDE) >= (VERTIPORT_SIDE + GATE_SIDE) and (length + SAFETY_SIDE) >= (VERTIPORT_SIDE + GATE_SIDE):
        if width >= (VERTIPORT_SIDE + GATE_SIDE):
            print("Large Enough Without Safety Area & Gate Ratio of 3 - Length Too Short")
            safety_needed = True 
            large_enough = True
            max_gate_ratio = 3
        elif length >= (VERTIPORT_SIDE + GATE_SIDE):
            print("Large Enough Without Safety Area & Gate Ratio of 3 - Width Too Short")
            safety_needed = True
            large_enough = True
            max_gate_ratio = 3
        else:
            print("Large Enough Without Safety Area & Gate Ratio of 3 - Both Too Short")
            safety_needed = True
            large_enough = True
            max_gate_ratio = 3
    elif (width + SAFETY_SIDE) >= (VERTIPORT_SIDE + GATE_SIDE) or (length + SAFETY_SIDE) >= (VERTIPORT_SIDE + GATE_SIDE):
        if width >= VERTIPORT_SIDE and length >= VERTIPORT_SIDE:
            print("Large Enough Without Safety Area & Gate Ratio of 2 - Longer Side Too Short")
            safety_needed = True
            large_enough = True
            max_gate_ratio = 2
        elif (width + SAFETY_SIDE) >= VERTIPORT_SIDE and (length + SAFETY_SIDE) >= VERTIPORT_SIDE:
            print("Large Enough Without Safety Area & Gate Ratio of 2 - Both Too Short")
            safety_needed = True
            large_enough = True
            max_gate_ratio = 2
    else:
        large_enough = False
    return(large_enough, safety_needed, max_gate_ratio)

#if width is longer, this function returns "True"
def findLongerSide(width, length):
    if width >= length:
        return(True)
    else:
        return(False)

#Check if short side long enough to double
def checkMaybeDouble(width, length):
    if findLongerSide(width, length) == True:
        #need to make sure the short side is long enough for one
        if length >= (VERTIPORT_SIDE + GATE_SIDE):
            if length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
                return(True)
            else:
                return(False)
        else:
            if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
                return(True)
            else:
                return(False)

    else:
        #need to make sure the short side is long enough for one
        if width >= (VERTIPORT_SIDE + GATE_SIDE):
            if width >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
                return(True)
            else:
                return(False)
        else:
            if length >= (VERTIPORT_SIDE * 2 + GATE_SIDE * 2):
                return(True)
            else:
                return(False)

#find number of vertiports based on gateToPadRatio
def checkVertiportsLinear(width, length):
    large_enough, safety_needed, max_gate_ratio = check_area_linear(areaWidth, areaLength)
    #Max Gate Ratio of 2 Without Safety
    if max_gate_ratio == 2 and safety_needed == True:
        vertiports3 = 0
        vertiports2 = 0
        vertiports3safety = 0
        vertiports2safety = 1
    #Max Gate Ratio of 2 With Safety
    elif max_gate_ratio == 2 and safety_needed == False:
        vertiports3 = 0
        vertiports2 = 1
        vertiports3safety = 0
        vertiports2safety = 1
    #Max Gate Ratio of 3 Without Safety
    elif max_gate_ratio == 3 and safety_needed == True:
        vertiports3 = 0
        vertiports2 = 1 #(144 + 72 - 48)/(144)
        vertiports3safety = 1
        vertiports2safety = 1 #(144 + 72)/(144)
    #Max Gate Ratio of 3 With Safety
    elif max_gate_ratio == 3 and safety_needed == False:
        vertiports3 = 1
        vertiports2 = 1 #(144 + 72)/(144)
        vertiports3safety = 1
        vertiports2safety = 1 #(144 + 72 + 48)/(144)
    #Regular
    else:
        if findLongerSide(width, length) == True:
            totalGates = math.floor(width/GATE_SIDE)
            vertiports3 = math.floor(totalGates/3)
            vertiports2 = math.floor(totalGates/2)
            totalGatesSafety = math.floor((width + SAFETY_SIDE)/GATE_SIDE)
            vertiports3safety = math.floor(totalGatesSafety/3)
            vertiports2safety = math.floor(totalGatesSafety/2)
        else:
            totalGates = math.floor(length/GATE_SIDE)
            vertiports3 = math.floor(totalGates/3)
            vertiports2 = math.floor(totalGates/2)
            totalGatesSafety = math.floor((length + SAFETY_SIDE)/GATE_SIDE)
            vertiports3safety = math.floor(totalGatesSafety/3)
            vertiports2safety = math.floor(totalGatesSafety/2)
    return(vertiports3, vertiports2, vertiports3safety, vertiports2safety)

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

large_enough, safety_needed, max_gate_ratio = check_area_linear(areaWidth, areaLength)

if large_enough == True:
    maybeDouble = checkMaybeDouble(areaWidth, areaLength)
    print("Short Side Long Enough To Double: " + str(maybeDouble))

    vertiports3, vertiports2, vertiports3safety, vertiports2safety = checkVertiportsLinear(areaWidth, areaLength)
    print(f"Vertiports With Ratio 3: {vertiports3}, Vertiports With Ratio 2: {vertiports2}")
    print(f"(Without Safety) Vertiports With Ratio 3: {vertiports3safety}, Vertiports With Ratio 2: {vertiports2safety}")

    numFlightsLinear3 = calculateFlights(areaWidth, areaLength, vertiports3, 4.66)
    numFlightsLinear2 = calculateFlights(areaWidth, areaLength, vertiports2, 5)
    numFlightsLinear3Safety = calculateFlights(areaWidth, areaLength, vertiports3safety, 4.66)
    numFlightsLinear2Safety = calculateFlights(areaWidth, areaLength, vertiports2safety, 5)
    print(f"Flights With Ratio 3: {numFlightsLinear3} Flights With Ratio 2: {numFlightsLinear2}")
    print(f"(Without Safety) Flights With Ratio 3: {numFlightsLinear3Safety} Flights With Ratio 2: {numFlightsLinear2Safety}")
    
else:
    print("Area Not Large Enough for Linear")

