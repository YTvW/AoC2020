import sys
import fileinput
from re import search
import time
bootSector = []
acc = 0

startTime = time.time()

for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n").split(" ")
    # print(cleanLine)
    bootSector.append(cleanLine)

PC = 0
linesExecuted = 0
instructionChanged = 0
instructionToChange= []
for Counter in range(len(bootSector)):
    if bootSector[Counter][0]== 'nop' or bootSector[Counter][0] == 'jmp':
        instructionToChange.append(Counter)


# print(instructionToChange)
try:
    for changes in instructionToChange:
        PC = 0
        linesExecuted = 0
        acc = 0
        while linesExecuted < len(bootSector)-1:
            # print(bootSector[PC])
            instruction = ""
            if changes == PC:
                # print("changing instruction")
                if bootSector[PC][0] == 'nop':
                    instruction = 'jmp'
                elif bootSector[PC][0] == 'jmp':
                    instruction = 'nop'
            else:
                instruction = bootSector[PC][0]
            value = int(bootSector[PC][1])
            # print("instruction: "+ instruction)
            # print("value: "+ str(value))  
            if instruction == 'nop':
                # print("nop")
                # bootSector[PC][0]=""
                PC +=1
                # print("PC: " + str(PC))
            elif instruction == 'jmp':
                # print("jmp")
                # bootSector[PC][0]=""
                PC += value
                # print("PC: " + str(PC))
            elif instruction == 'acc':
                # print("acc")
                acc += value
                # bootSector[PC][0]=""
                PC +=1
                # print("PC: " + str(PC))
            else:
                break
            
            linesExecuted +=1
except IndexError:
    print("acc: "+ str(acc))
    print("--- %s seconds ---" % (time.time() - startTime))