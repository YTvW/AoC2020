import sys
import fileinput
from re import search
import time
startTime = time.time()
inputData =[0,14,6,20,1,4]
# inputData = [0,3,6]

def updateNumbers(num):
    # print("num: " + str(num))
    # print("len: "+str(len(spokenNumbers[num])))
    # print("history: "+str(spokenNumbers[num]))
    # print("round: "+ str(round))

    
    if len(spokenNumbers[num]) >= 2:
        # print("calculating next value1: " + str(spokenNumbers[num][1] - spokenNumbers[num][0]))
        # nextValue = spokenNumbers[num][1] - spokenNumbers[num][0]
        spokenNumbers[num][0] = spokenNumbers[num][1]
        spokenNumbers[num][1] = round
        nextValue = spokenNumbers[num][1] - spokenNumbers[num][0]
        # print("calculating next value:2 " + str(spokenNumbers[num][1] - spokenNumbers[num][0]))
        return nextValue
    else:
        spokenNumbers[num].append(round)
        return spokenNumbers[num][1] - spokenNumbers[num][0]

    

def inserNewNumber(num):
    spokenNumbers[num].append(0)

lastSpoken = 0
spokenNumbers ={}
spokenOrder =[]
round = 1
while round < 30000000:
    
    if len(inputData) >0:
        lastSpoken = inputData[0]
        inputData.remove(lastSpoken)

    try:
        previousRound  = spokenNumbers[lastSpoken]
        lastSpoken = updateNumbers(lastSpoken)
        # print("round: "+ str(round) + " NRSpoken: " +str(lastSpoken)+ " spokenNumbers: " +str(spokenNumbers))
    except KeyError as identifier:
        # print("number is new")
        spokenNumbers[lastSpoken] = [round]
        lastSpoken = 0
        # print("round: "+ str(round) + " NRSpoken: " +str(lastSpoken)+ " spokenNumbers: " +str(spokenNumbers))
    spokenOrder.append(lastSpoken)
    round+=1

print(round)
print(lastSpoken)
# print(spokenOrder)
# print("round: "+ str(round) + " NRSpoken: " +str(lastSpoken)+ " spokenNumbers: " +str(spokenNumbers))
print("--- %s seconds ---" % (time.time() - startTime))