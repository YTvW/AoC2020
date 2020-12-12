import sys
import fileinput
from re import search
import time
startTime = time.time()

seatIds = []
highestId = 0
for line in fileinput.input("./input5.txt"):
    rows = []
    colums= []
    for row in range(128):
        rows.append(row)
    for colum in range(8):
        colums.append(colum)


    for char in line:
        if char == "F":
            rows = rows[0:len(rows)/2]
        elif char == "B":
            rows = rows[len(rows)/2:len(rows)]
        elif char == "L":
            colums = colums[0:len(colums)/2]
        elif char == "R":
            colums = colums[len(colums)/2:len(colums)]
            
        pass

    seatId = rows[0]*8 + colums[0]
    if seatId > highestId:
        highestId = seatId
    seatIds.append(seatId)

seatIds.sort()
total = 0;
lastTotal = seatIds[0]

for entry in range(len(seatIds)-1):
    if seatIds[entry]+1 != seatIds[entry+1]:
        print("this is my seat: " + str(seatIds[entry]+1))
        break; 

print(highestId)
print("--- %s seconds ---" % (time.time() - startTime))