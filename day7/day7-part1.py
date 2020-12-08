import sys
import fileinput
from re import search
import time
startTime = time.time()
sum = 0
allBags = []
level1bags = []
level2bags = []
group = []


def findBags(data, dataToCheck):
    temp = []
    global sum
    for bags in dataToCheck:
        bag = bags.split(" ")[0] +" "+ bags.split(" ")[1]
        # print(bag)
        for items in data:
            inside = items.split("contain")[1]
            if inside.count(bag):
                # print("YES")
                temp.append(items)
    temp =list(dict.fromkeys(temp))
    if len(temp) > 0:
        # print(len(temp))
        sum += len(temp)
        for item in temp:
            data.remove(item)
        findBags(data,temp)
    else:
        return True

for line in fileinput.input("./input7.txt"):
    inside = line.split("contain")[1]
    if inside.count("shiny gold"):
        level1bags.append(line.encode("utf-8").strip("\n"))
        sum +=1
    else:
        allBags.append(line.encode("utf-8").strip("\n"))


findBags(allBags,level1bags)

print("result: " + str(sum))
print("--- %s seconds ---" % (time.time() - startTime))