import sys
import fileinput
from re import search
import time
startTime = time.time()
inputData =[0,14,6,20,1,4]
# inputData = [0,3,6]

def updateNumbers(num):
    if len(spokenNumbers[num]) >= 2:
        spokenNumbers[num][0] = spokenNumbers[num][1]
        spokenNumbers[num][1] = round
        nextValue = spokenNumbers[num][1] - spokenNumbers[num][0]
        return nextValue
    else:
        spokenNumbers[num].append(round)
        return spokenNumbers[num][1] - spokenNumbers[num][0]

lastSpoken = 0
spokenNumbers ={}
round = 1

while round < 30000000:
    
    if len(inputData) >0:
        lastSpoken = inputData[0]
        inputData.remove(lastSpoken)

    try:
        previousRound  = spokenNumbers[lastSpoken]
        lastSpoken = updateNumbers(lastSpoken)
    except KeyError as identifier:
        spokenNumbers[lastSpoken] = [round]
        lastSpoken = 0
    round+=1

print("round: "+ str(round) + " result: " +str(lastSpoken))
print("--- %s seconds ---" % (time.time() - startTime))