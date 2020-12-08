import sys
import fileinput
from re import search
import time
startTime = time.time()
sum = 0
group = []
for line in fileinput.input("./input6.txt"):
    if line == "\n":
        group = list(dict.fromkeys(group))
        # print(len(group))
        sum += len(group)
        group = [ ]
    if line != "\n":
        group.extend(list(line.encode("utf-8").strip("\n")))

print("result: " + str(sum))
print("--- %s seconds ---" % (time.time() - startTime))