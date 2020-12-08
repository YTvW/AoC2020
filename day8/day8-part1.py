import sys
import fileinput
from re import search
import time
startTime = time.time()
bootSector = []
acc = 0
for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n").split(" ")
    # print(cleanLine)
    bootSector.append(cleanLine)

PC = 0
linesExecuted = 0
while linesExecuted < len(bootSector):
    # print(bootSector[PC])
    instruction = bootSector[PC][0]
    value = int(bootSector[PC][1])
    # print("instruction: "+ instruction)
    # print("value: "+ str(value))
    if instruction == 'nop':
        # print("nop")
        bootSector[PC][0]=""
        PC +=1
        # print("PC: " + str(PC))
    elif instruction == 'jmp':
        # print("jmp")
        bootSector[PC][0]=""
        PC += value
        # print("PC: " + str(PC))
    elif instruction == 'acc':
        # print("acc")
        acc += value
        bootSector[PC][0]=""
        PC +=1
        # print("PC: " + str(PC))
    else:
        break
    
    linesExecuted +=1
print(acc)
print("--- %s seconds ---" % (time.time() - startTime))