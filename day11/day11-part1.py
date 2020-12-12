import sys
import fileinput
from re import search
import time
import numpy as np
startTime = time.time()
dataList = []
lineLength = 0

for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    lineLength = len(cleanLine)
    for char in cleanLine:
        if char == "L":
            dataList.append(int(0))
        elif char == ".":
            dataList.append(int(-1))

lines = len(dataList)/lineLength

def checkSeats(data,row,colum):
    ocupiedSeats=0
    currentSeat = checkSeat(data,row, colum)
    if currentSeat == -1:
        return currentSeat
    elif currentSeat == 0:
        for rows in range(row -1,row+2):
            for colums in range(colum -1,colum+2):
                status = checkSeat(data,rows, colums)
                if status == 1:
                    return currentSeat
    elif currentSeat == 1:
        for rows in range(row -1,row+2):
            for colums in range(colum -1,colum+2):
                status = checkSeat(data,rows, colums)
                if status == 1 and ocupiedSeats >= 5:
                    return 0
                elif status == 1:
                    ocupiedSeats+=1
    
    if currentSeat == 0 and ocupiedSeats == 0:
        return 1
    elif currentSeat == 1 and ocupiedSeats >= 5:
        return 0
    else:
        return currentSeat


def checkSeat(data,row,colum):
    
    if row in range(lines):
        if colum in range(lineLength):
            return data[colum+row*lineLength]
    #     else:
    #         return 99
    # else:
    #     return 99

def checkList(data,oldCount):
    newList = []
    for line in range(lines):
        for i in range(lineLength):
            result = checkSeats(data,line,i)
            newList.append(result)
    occupiedSeats = newList.count(1)
    if occupiedSeats != oldCount:
        return checkList(newList,occupiedSeats)
    else:
        return occupiedSeats

print("result: "+str(checkList(dataList,0)))

print("--- %s seconds ---" % (time.time() - startTime))