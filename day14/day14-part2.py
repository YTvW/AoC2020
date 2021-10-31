import sys
import fileinput
from re import search
import time
from itertools import product
startTime = time.time()

programs = []
program = []
programstruct = {
    "mask": "",
    "operations": []
}
memory = {}


# for line in fileinput.input("./input.txt"):
for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8")

    match = search("^(mask)\s=\s([0,1,X]{36})$|^(mem)\[([0-9]*)\]\s=\s([0-9]*)$",cleanLine.strip("\n"))
    match.group(0)
    if cleanLine == "\n":
        programs.append(programstruct)

    if match.group(1) == "mask" and programstruct["mask"] != "":
        programs.append(programstruct)
        # mask = []
        lastIndex = 0
        tempRange = []
        for x in range(36):
            if match.group(2)[x] != lastIndex:#and match.group(2)[x] == "X":
                
        print(match.group(2))

        programstruct =  {
            "mask": match.group(2),
            "operations": []
        }
    elif match.group(1) == "mask":
        # for x in range(match.group(2).count("X")):
        #     # match.group(2)
        #     print("found X")
        programstruct["mask"] = match.group(2)
    else:
        programstruct["operations"].append((int(match.group(4)),int(match.group(5))))
    
programs.append(programstruct)




for items in programs:
    set1Mask = items["mask"].replace("X","0")
    set0Mask = items["mask"].replace("X","1")

    # print(items["mask"])
    # print(set1Mask)
    # print(set0Mask)
    # print(items)
    for ops in items["operations"]:
        # print(ops)
        # print(bin(ops[1]))
        temp = ops[1] | int(set1Mask, 2)
        temp = temp & int(set0Mask, 2)
        memory[ops[0]]=temp
        # print(temp)
        # print(bin(temp))

values = memory.values()
total = sum(values)

print(len(programs))
print("result = "+str(total))
print("--- %s seconds ---" % (time.time() - startTime))