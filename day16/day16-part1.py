import sys
import fileinput
from re import search
import time
startTime = time.time()
ranges = []
nearby_tickets = []
lowestRange = 10000000000000000000
highestRange = 0
groupDelimiter = False




# for line in fileinput.input("./test.txt"):
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    match = search("^([a-z\s]*):\s([0-9\-]*)\sor\s([0-9\-]*)|^([a-z\s]*:$)|(^[0-9,]+$)",cleanLine)
    if match  != None:

        if match.group(1)!= None:
            rangeList =match.group(2).split("-")
            # ranges.append((int(rangeList[0]),int(rangeList[1])))
            if int(rangeList[0]) < lowestRange:
                lowestRange = int(rangeList[0])
            elif int(rangeList[1]) > highestRange:
                highestRange = int(rangeList[1])
            rangeList =match.group(3).split("-")
            # ranges.append((int(rangeList[0]),int(rangeList[1])))
            if int(rangeList[0]) < lowestRange:
                lowestRange = int(rangeList[0])
            elif int(rangeList[1]) > highestRange:
                highestRange = int(rangeList[1])


        elif match.group(4)!= None:
            # print(match.group(4))
            groupDelimiter =True
        elif match.group(5)!=None:
            number_list = match.group(5).split(",")
            map_object = map(int, number_list)
            nearby_tickets.append(list(map_object))
            # print(match.group(5))
        else:
            groupDelimiter = False
    # print(cleanLine)

# print(lowestRange)
# print(highestRange)
# print(nearby_tickets)
errorRate = 0
for ticket in nearby_tickets:
    # ticket.sort()
    # print(ticket)
    for nr in ticket:
        if nr < lowestRange or nr > highestRange:
            errorRate += nr

print("errorRate: " + str(errorRate))

print("--- %s seconds ---" % (time.time() - startTime))