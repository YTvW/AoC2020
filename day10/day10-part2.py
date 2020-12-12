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
    # print(line.encode("utf-8").strip("\n"))

options = 0
invalidOptions = 0
adapterList.sort()
adapterList.insert(0,0)
adapterList.append(adapterList[-1]+3)
print(adapterList)
maxValue = adapterList[-1]
print("maxValue: " + str(maxValue))
maxLength = maxValue/1
minLength = maxValue/3
option = {
    "currentValue": 0,
    "optionNumber": 0,
    "nextOptions": [],
}

def getNextOptions(input,offset,optionNumber):
    nextOptions = []
    for i in range(1,3):
        if input[offset+i] - input[offset] <= 3:
            nextOptions.append({
            "currentValue": input[offset],
            "optionNumber": optionNumber+1,
            "nextOptions": getNextOptions,
            })
            print("valid Option")
    
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
        # print(temp)
        splitList.append(temp)
        temp = []

print(splitList)
count = 0
totals = []
listCount = 0
allcombos = []
for items in splitList:
    offset = 0
    combs = []
    length = len(items)
    while length > 0:
        combs.append(combinations(items,length))
        length -= 1
    # print(list(combs))
    #remove invalid combinations
    count =0
    for it in combs:
        for opt in it:
            # print(opt)
            if items[0] == opt[0] and items[-1] == opt[-1]:
                diff = [opt[i+1]-opt[i] for i in range(len(opt)-1)]
                if diff.count(3) + diff.count(2) + diff.count(1) == len(diff):
                    print(opt)
                    print("valid")
                    count+=1
    
    totals.append(count)
    
# for items in allcombos:
# items = allcombos[0]

# for items in allcombos:
#     count =0
    
#     for it in items:
#         # print([it[i+1]-it[i] for i in range(len(it)-1)])
#         print(list(it))
#         # print(it[0])
#         # print(splitList[listCount])
#         #checkif combo is valid
#         # if splitList[listCount][0] == it[0] and splitList[listCount][-1] == it[-1]:
#         #     print("testing")


#         count+=1
#     listCount+=1
#     totals.append(count)
    # break;

print(multiplyList(totals))


    # for it in combos:
    #     # print(len(it))
    #     # print(it[-1])
    #     com+=1
        # if len(it) == 0 or it[0] != 0 or it[-1] != maxValue:
        #     # print("not a valid option") 
        #     # print(it[0])
        #     # print(it[-1])
        #     invalidOptions +=1
        
        # else:
        #     # print(it)
        #     diff = [it[i+1]-it[i] for i in range(len(it)-1)]
        #     # print(len(diff))
        #     # print(len(diff) - diff.count(3)+diff.count(2)+diff.count(1))
        #     if len(diff) - (diff.count(3)+diff.count(2)+diff.count(1)) == 0:
        #         # print(it)
        #         optionsList.append(it)
        #         options += 1
#             # print(diff.count(2))
#             # print(diff.count(1))

#             # if diff.count(4) >= 1:
#             #     # print("not a valid option")
#             #     invalidOptions +=1
#             # else:
#             #     optionsList.append(it)
#             #     options += 1

# print(optionsList)

print("options: " + str(options))
# adapterList.insert(0,0)
# adapterList.append(adapterList[-1]+3)
# diff = [adapterList[i+1]-adapterList[i] for i in range(len(adapterList)-1)]
# diff3 = diff.count(3)
# diff1 = diff.count(1) 

# print("result:" + str(diff1*diff3))
[0, 1, 2, 3, 4]
[0, 2, 3, 4]
[0, 3, 4]
[0, 1, 3, 4]
[0, 1, 4]
[0, 1, 2, 4]
[0, 2, 4]

print("--- %s seconds ---" % (time.time() - startTime))