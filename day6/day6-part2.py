import sys
import fileinput
from re import search
import time
startTime = time.time()
sum = 0
group = []
lines = 0
for line in fileinput.input("./input6.txt"):
    if line == "\n":
        for item in list(dict.fromkeys(group)):
            answered = group.count(item)
            if answered == lines:
                sum += 1
            pass

        lines = 0 
        group = [ ]
    if line != "\n":
        group.extend(list(line.encode("utf-8").strip("\n")))
        lines += 1

print("result: " + str(sum))
print("--- %s seconds ---" % (time.time() - startTime))