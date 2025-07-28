import math

#change to be able to import table of places & export same table but with data on different configurations
#output a graph of different configurations and their throughput - build upon other research paper
#determines which topology is best for a space depending on - size, width/length ratio,
#Include different configurations

area_width = 150 #ft
area_length = 350 #ft
flight_time = 10 #min
#an air taxi can be on each section at the same time so the total time will be shorter
flight_time_triple = 3.5 #min

#drop-off/pick-up can be smaller because it does not need the safety area (Double check w/research)
VERTIPORT_WIDTH_TRIPLE = 100 + 50 + 100 #ft
VERTIPORT_WIDTH = 100 #ft
#regular vertiport size + waiting area
VERTIPORT_LENGTH = 100 + 10 #ft
#area = area_length * area_width

#checking that the given area is big enough for a vertiport
def check_area(width, length):
    if width >= VERTIPORT_WIDTH and length >= VERTIPORT_WIDTH:
        if width >= VERTIPORT_LENGTH or length >= VERTIPORT_LENGTH:
            #print("Large enough for vertiport and waiting area")
            return(True)
        else:
            #print("Only Large enough for vertiport")
            return(False)
    else:
        #print("Not large enough for a vertiport")
        return(False)

#calculate number of vertiports with one area for landing, dropoff, & takeoff
def calculate_vertiports_single(width, length):
    #find the longer side
    if width >= length:
    #Make ony 100 x 110 ft boxes of vertiports and not include excess areas
        number_width = math.floor(width/VERTIPORT_LENGTH)
        number_length = math.floor(length/VERTIPORT_WIDTH)
        number_vertiports = number_width * number_length
        return(number_vertiports)
    else:
        number_width = math.floor(width/VERTIPORT_WIDTH)
        number_length = math.floor(length/VERTIPORT_LENGTH)
        number_vertiports = number_width * number_length
        return(number_vertiports)
    
#calculate number of vertiports with different area for landing, dropoff, & takeoff
def calculate_vertiports_triple(width, length):
    #find the longer side
    if length >= width:
    #Make ony 100 x 110 ft boxes of vertiports and not include excess areas
        number_width = math.floor(width/VERTIPORT_LENGTH)
        number_length = math.floor(length/(VERTIPORT_WIDTH_TRIPLE))
        number_vertiports = number_width * number_length
        return(number_vertiports)
    else:
        number_width = math.floor((width/VERTIPORT_WIDTH_TRIPLE))
        number_length = math.floor(length/VERTIPORT_LENGTH)
        number_vertiports = number_width * number_length
        return(number_vertiports)
    
#calculates flights per hour based on minutes per flight
def calculate_flights(vertiports, time):
    flights = 60/time * vertiports
    return(flights)


if check_area(area_width, area_length) == True:
    print("Given The Same Area:")
    vertiports = calculate_vertiports_single(area_width, area_length)
    flights_single = calculate_flights(vertiports, flight_time)
    
    print( "Number of Vertiports (Single Config): " + str(vertiports))
    print("Number of Flights Per Hour (Single Config): " + str(flights_single))

    vertiports_triple = calculate_vertiports_triple(area_width, area_length)
    flights_triple = calculate_flights(vertiports_triple, flight_time_triple)

    print( "Number of Vertiports (Triple Config): " + str(vertiports_triple))
    print("Number of Flights Per Hour (Triple Config): " + str(flights_triple))
