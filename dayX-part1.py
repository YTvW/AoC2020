import sys
import fileinput
from re import search
import time
startTime = time.time()
for line in fileinput.input("./input7.txt"):
    print(line)


print("--- %s seconds ---" % (time.time() - startTime))