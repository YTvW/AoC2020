import sys
import fileinput
from re import search
import time
startTime = time.time()
ranges = []
nearby_tickets = []
lowestRange = 10000000000000000000
highestRange = 0
groupDelimiter = False
fields = {}
fieldOrder = {}

def CheckField(value):
    temp = []
    # print(value)
    for items in fields:
        l1l = fields[items][0][0]
        l1h = fields[items][0][1]
        l2l = fields[items][1][0]
        l2h = fields[items][1][1]
        
        if (value >= l1l and value <= l1h) or (value >= l2l and value <= l2h):
            temp.append(items)
    return temp

# for line in fileinput.input("./test.txt"):
for line in fileinput.input("./input.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    match = search("^([a-z\s]*):\s([0-9\-]*)\sor\s([0-9\-]*)|^([a-z\s]*:$)|(^[0-9,]+$)",cleanLine)
    if match  != None:

        if match.group(1)!= None:
            rangeList1 =match.group(2).split("-")
            rangeList2 =match.group(3).split("-")
            fields[match.group(1)] = [(int(rangeList1[0]),int(rangeList1[1])),(int(rangeList2[0]),int(rangeList2[1]))]
            
            if int(rangeList1[0]) < lowestRange:
                lowestRange = int(rangeList1[0])
            elif int(rangeList1[1]) > highestRange:
                highestRange = int(rangeList1[1])
            if int(rangeList2[0]) < lowestRange:
                lowestRange = int(rangeList2[0])
            elif int(rangeList2[1]) > highestRange:
                highestRange = int(rangeList2[1])

        elif match.group(4)!= None:
            groupDelimiter =True
        elif match.group(5)!=None:
            number_list = match.group(5).split(",")
            map_object = map(int, number_list)
            nearby_tickets.append(list(map_object))
        else:
            groupDelimiter = False

invalidTickets = []
errorRate = 0
for i in range(len(nearby_tickets)):
    ticket = nearby_tickets[i]
    invalid = False
    for nr in ticket:
        if nr < lowestRange or nr > highestRange:
            errorRate += nr
            invalid = True
    if invalid:
        invalidTickets.append(ticket)

for i in invalidTickets:
    nearby_tickets.remove(i)

colums = {}

for i in range(len(nearby_tickets[0])):
    colums[i] = []
    for j in range(len(nearby_tickets)):
        valueToCheck = nearby_tickets[j][i] 
        validFields = CheckField(valueToCheck)
        colums[i].append(validFields)

selectedFields = {}
while len(selectedFields.keys()) != len(nearby_tickets[0]):
    for keys in colums:

        options = colums[keys]
        counted_fields = {}
        mostCounted = 0
        for opt in options:
            for f in selectedFields:
                if opt.count(f) >=1:
                    opt.remove(f)
            for fields in opt:
                try:
                    foundFields = counted_fields.keys()
                    if foundFields.count(fields) >=1:
                        counted_fields[fields] +=1
                    else:
                        counted_fields[fields] = 1
                except expression as identifier:
                    counted_fields[fields] = 1
        validFields = []
        all_values = counted_fields.values()
        if len(all_values)>=1:
            max_value = max(all_values)
            for key, value in counted_fields.items():
                if value == max_value:
                    validFields.append(key)
            if len(validFields) == 1:
                print("adding new field")
                selectedFields[validFields[0]] = keys
                colums[keys] = []

result = 1
for item in selectedFields:
    if item.startswith("departure"):
        result *= nearby_tickets[0][selectedFields[item]]

print("errorRate: " + str(errorRate))
print("result: " + str(result))
print("--- %s seconds ---" % (time.time() - startTime))