import sys
import fileinput
from re import search
import time
startTime = time.time()
info = []
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    info.append(cleanLine)
    print(cleanLine)

expectedTime = int(info[0])
busses = info[1].split(",")
busses = list(dict.fromkeys(busses))
busses.remove("x")
closest = int(busses[-1])
bus = 0

for bus in busses:
    res = expectedTime % int(bus)
    nextTime = expectedTime+ (int(bus)-res) 
    waitTime = nextTime - expectedTime
    if nextTime - expectedTime < closest:
        closest= waitTime
        bus = int(bus)
    
print("result: " + str(closest*bus))
print("--- %s seconds ---" % (time.time() - startTime))