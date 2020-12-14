import sys
import fileinput
from re import search
import time
startTime = time.time()

programs = []
program = []
programstruct = {
    "mask": "",
    "operations": []
}
memory = {}

for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8")
    match = search("^(mask)\s=\s([0,1,X]{36})$|^(mem)\[([0-9]*)\]\s=\s([0-9]*)$",cleanLine.strip("\n"))
    if cleanLine == "\n":
        programs.append(programstruct)

    if match.group(1) == "mask" and programstruct["mask"] != "":
        programs.append(programstruct)
        programstruct =  {
            "mask": match.group(2),
            "operations": []
        }
    elif match.group(1) == "mask":
        programstruct["mask"] = match.group(2)
    else:
        programstruct["operations"].append((int(match.group(4)),int(match.group(5))))
    
programs.append(programstruct)

for items in programs:
    set1Mask = int(items["mask"].replace("X","0"),2)
    set0Mask = int(items["mask"].replace("X","1"),2)
    for ops in items["operations"]:
        temp = ops[1] | set1Mask
        temp = temp & set0Mask
        memory[ops[0]]=temp

values = memory.values()
total = sum(values)

print("result = "+str(total))
print("--- %s seconds ---" % (time.time() - startTime))