import sys
import fileinput
from re import search
import time
startTime = time.time()
adapterList = []

for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    adapterList.append(int(line.encode("utf-8").strip("\n")))
    # print(line.encode("utf-8").strip("\n"))

adapterList.sort()
adapterList.insert(0,0)
adapterList.append(adapterList[-1]+3)
diff = [adapterList[i+1]-adapterList[i] for i in range(len(adapterList)-1)]
diff3 = diff.count(3)
diff1 = diff.count(1) 
print("result:" + str(diff1*diff3))

print("--- %s seconds ---" % (time.time() - startTime))