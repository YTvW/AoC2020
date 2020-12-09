import sys
import fileinput
from re import search
import json
import time
startTime = time.time()
sum = 0
allBags = []
level1bags = []
level2bags = []
group = []
bagObjs = []


# for line in fileinput.input("./test7.2.txt"):
for line in fileinput.input("./input7.txt"):
    inside = line.split("contain")[0]
    if inside.count("shiny gold bags"):
        level1bags.append(line.encode("utf-8").strip("\n").split("contain"))
    else:
        allBags.append(line.encode("utf-8").strip("\n").split(" contain"))

def findBags(data,check):

    for item in data:
        if str(item[0]) == str(check):
            bagz=[]
            inside = item[1]
            insides = inside.split(",")
            for bags in insides:
                match = search("([0-9]{1})\s([a-z]+\s[a-z]+\s[a-z]+)",bags)
                colour=""
                if match == None:
                    return None
                if match.group(1).split(" ")[0] == str(1):
                    colour = match.group(2)+ "s"
                else:
                    colour = match.group(2)
                bag= {
                    "count": match.group(1),
                    "colour": colour,
                    "contrib": 0,
                    "contains": findBags(allBags,colour)
                }
                bagz.append(bag)
            return bagz

for item in level1bags:
    inside = item[1]
    insides = inside.split(",")
    for bags in insides:
        match = search("([0-9]{1})\s([a-z]+\s[a-z]+\s[a-z]+)",bags)
        colour=""
        # print(match.group(1).split(" ")[0])
        if int(match.group(1).split(" ")[0]) == 1:
            # print("single bag")
            colour = match.group(2)+ "s"
            # print(colour)
        else:
            colour = match.group(2)

        bag= {
            "count": match.group(1),
            "colour": colour,
            "contrib": 0,
            "contains": findBags(allBags,colour)
        }
        bagObjs.append(bag)

sum = 0
rootbag  = {
    "count": "1",
    "colour": "shiny gold bags",
    "contains": bagObjs,
    "contrib": 1
}

def calcContrib(root):
    for bags in root["contains"]:
        bags['contrib'] += int(bags['count']) * int(root['contrib'])
        # print(bags['contrib'])
        if bags['contains'] != None:
            # print("nextLevel")
            calcContrib(bags)

calcContrib(rootbag)

def calcTotal(root):
    global sum
    for bags in root["contains"]:
        # print(bags['contrib'])
        sum += bags['contrib']
        if bags['contains'] != None:
            # print("nextLevel")
            calcTotal(bags)
    
# print(json.dumps(rootbag))
calcTotal(rootbag)
print("result: " + str(sum))
print("--- %s seconds ---" % (time.time() - startTime))