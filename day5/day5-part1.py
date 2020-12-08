import sys
import fileinput
from re import search
import time
startTime = time.time()


# rows = []
# for row in range(128):
#     rows.append(row)
#     print(rows[row])
seatIds = []
highestId = 0
for line in fileinput.input("./input5.txt"):
    rows = []
    colums= []
    for row in range(128):
        rows.append(row)
        # print(rows[row])
    for colum in range(8):
        colums.append(colum)
        # print(colums[colum])

    for char in line:
        if char == "F":
            rows = rows[0:len(rows)/2]
            # print(rows)
        elif char == "B":
            rows = rows[len(rows)/2:len(rows)]
        elif char == "L":
            colums = colums[0:len(colums)/2]
        elif char == "R":
            colums = colums[len(colums)/2:len(colums)]
            
        pass
    # print(rows)
    # print(colums)
    seatId = rows[0]*8 + colums[0]
    if seatId > highestId:
        highestId = seatId
    # print(seatId)
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