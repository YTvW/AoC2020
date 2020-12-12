import sys
import fileinput
from re import search
import time
from itertools import combinations
startTime = time.time()
adapterList = []
optionsList = []

for line in fileinput.input("./input.txt"):
# for line in fileinput.input("./test.txt"):
    adapterList.append(int(line.encode("utf-8").strip("\n")))

adapterList.sort()
adapterList.insert(0,0)
adapterList.append(adapterList[-1]+3)

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

splitList = []
temp = []
for i in range(len(adapterList)-1):
    if adapterList[i+1] - adapterList[i] < 3:
        temp.append(adapterList[i])
    else:
        temp.append(adapterList[i])
        splitList.append(temp)
        temp = []


count = 0
totals = []

for items in splitList:
    offset = 0
    combs = []
    length = len(items)
    while length > 0:
        combs.append(combinations(items,length))
        length -= 1

    count =0
    for it in combs:
        for opt in it:
            # print(opt)
            if items[0] == opt[0] and items[-1] == opt[-1]:
                diff = [opt[i+1]-opt[i] for i in range(len(opt)-1)]
                if diff.count(3) + diff.count(2) + diff.count(1) == len(diff):
                    # print(opt)
                    # print("valid")
                    count+=1
    totals.append(count)
    
print(multiplyList(totals))

print("--- %s seconds ---" % (time.time() - startTime))