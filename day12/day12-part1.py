import sys
import fileinput
from re import search
import time
startTime = time.time()

currentDir = "E"
directions = {
     0:"N" ,
    90:"E",
    180:"S",
    270:"W"
}
tempPos = 90
currentPos = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}


def updateDirection(val):
    global tempPos
    tempPos += val
    return directions[tempPos%360]

# def updatePos()

# for line in fileinput.input("./test.txt"):
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    # print(cleanLine)
    match =search("^([F,N,E,S,W,R,L]{1})([0-9]*)$",cleanLine)
    
    if match.group(1) == "F":
        # print("forward: " + match.group(2))
        currentPos[currentDir] += int(match.group(2))
    elif match.group(1) == "R":
        currentDir= updateDirection( int(match.group(2)))
    elif match.group(1) == "L":
        currentDir= updateDirection(- int(match.group(2)))
    else:
        currentPos[match.group(1)] += int(match.group(2))
        # print(match.group(1))
    # print(currentDir)
        
# print(currentPos)
# print(abs(currentPos["E"]-currentPos["W"]))
# print(abs(currentPos["N"]-currentPos["S"]))
print("result: " +str(abs(currentPos["N"]-currentPos["S"]) + abs(currentPos["E"]-currentPos["W"])))
print("--- %s seconds ---" % (time.time() - startTime))