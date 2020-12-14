import sys
import fileinput
from re import search
import time
startTime = time.time()

inputData = []
preambleSize = 25
preambleData = []
invalidEntry = 0
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    # print(cleanLine)
    inputData.append(int(cleanLine))


for i in range(len(inputData)):
    if i < preambleSize:
        preambleData.append(inputData[i])
    else:
        found = False
        for numbers in preambleData:
            remain = inputData[i] - numbers
            # print(remain)
            if preambleData.count(remain) == 1:
                # print("OK")
                found = True
                pass
        if not found:
            invalidEntry = inputData[i]
            break;
        preambleData.pop(0)
        preambleData.append(inputData[i])

print(str(invalidEntry) + " is not confirm preamble")
print("--- part1: %s seconds ---" % (time.time() - startTime))

for i in range(len(inputData)):
    continousValues= []
    sum = 0
    offset = 0
    while sum < invalidEntry:
        sum += inputData[i+offset]
        continousValues.append(inputData[i+offset])
        # print(inputData[i+offset])
        offset +=1
    if sum == invalidEntry and len(continousValues)> 1:
        continousValues.sort()
        print("result: " + str(continousValues[0] + continousValues[-1]))
        # print(str(continousValues) + " is list")
        pass
    # elif sum < invalidEntry:
    #     print(continousValues)
    #     print(len(continousValues))
    # print(continousValues)

# print(str(invalidEntry) + " is not confirm preamble")
print("--- part2: %s seconds ---" % (time.time() - startTime))