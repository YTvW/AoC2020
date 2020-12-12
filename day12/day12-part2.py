import sys
import fileinput
from re import search
import time
startTime = time.time()

currentPos = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}

wayPointPos = {
    "N": 1, 
    "E": 10,
    "S": 0,
    "W": 0
}

def rotateWaypointR(val):
    global wayPointPos
    steps = val/90
    tempWayPointPos = {}
    if steps == 1:
        tempWayPointPos["N"] = wayPointPos["W"]
        tempWayPointPos["E"] = wayPointPos["N"]
        tempWayPointPos["S"] = wayPointPos["E"]
        tempWayPointPos["W"] = wayPointPos["S"]
    elif steps == 2:
        tempWayPointPos["N"] =wayPointPos["S"]
        tempWayPointPos["E"] =wayPointPos["W"]
        tempWayPointPos["S"] =wayPointPos["N"]
        tempWayPointPos["W"] =wayPointPos["E"]
    elif steps == 3:
        tempWayPointPos["N"] =wayPointPos["E"]
        tempWayPointPos["E"] =wayPointPos["S"]
        tempWayPointPos["S"] =wayPointPos["W"]
        tempWayPointPos["W"] =wayPointPos["N"]
    wayPointPos = tempWayPointPos

def rotateWaypointL(val):
    global wayPointPos
    steps = val/90
    tempWayPointPos = {}
    if steps == 1:
        tempWayPointPos["N"] = wayPointPos["E"]
        tempWayPointPos["E"] = wayPointPos["S"]
        tempWayPointPos["S"] = wayPointPos["W"]
        tempWayPointPos["W"] = wayPointPos["N"]
    elif steps == 2:
        tempWayPointPos["N"] =wayPointPos["S"]
        tempWayPointPos["E"] =wayPointPos["W"]
        tempWayPointPos["S"] =wayPointPos["N"]
        tempWayPointPos["W"] =wayPointPos["E"]
    elif steps == 3:
        tempWayPointPos["N"] =wayPointPos["W"]
        tempWayPointPos["E"] =wayPointPos["N"]
        tempWayPointPos["S"] =wayPointPos["E"]
        tempWayPointPos["W"] =wayPointPos["S"]
    wayPointPos = tempWayPointPos

def getActualPos():
    actPos = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
    }
    EW = wayPointPos["E"] - wayPointPos["W"]
    NS = wayPointPos["N"] - wayPointPos["S"]
    if EW >1:
        actPos["E"] = EW
    else:
        actPos["W"] = -EW
    if NS >=1:
        actPos["N"] = NS
    else:
        actPos["S"] = -NS
    
    return actPos

lineNr = 0
# for line in fileinput.input("./test.txt"):
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    match =search("^([F,N,E,S,W,R,L]{1})([0-9]*)$",cleanLine)
    lineNr += 1
    if match.group(1) == "F":
        movePos = getActualPos()
        currentPos["N"] += wayPointPos["W"]*int(match.group(2))
        currentPos["E"] += wayPointPos["N"]*int(match.group(2))
        currentPos["S"] += wayPointPos["E"]*int(match.group(2))
        currentPos["W"] += wayPointPos["S"]*int(match.group(2))
    elif match.group(1) == "R":
        rotateWaypointR(int(match.group(2)))
    elif match.group(1) == "L":
        rotateWaypointL(int(match.group(2)))
    else:
        wayPointPos[match.group(1)] += int(match.group(2))

print("result: " +str(abs(currentPos["N"]-currentPos["S"]) + abs(currentPos["E"]-currentPos["W"])))
print("--- %s seconds ---" % (time.time() - startTime))