import sys
import fileinput
from re import search
import time
startTime = time.time()

pocket_dimension = [[[0,0,0],[0,0,0],[0,0,0]],[],[[0,0,0],[0,0,0],[0,0,0]]]


def checkPositioin(z,r,c):
    activeNeighbours = 0
    inactiveNeighbours = 0
    for zs in range(z-1,z+2):
        # print("zs "+str(zs))
        for rs in range(r-1,r+2):
            # print("rs "+str(rs))
            for cs in range(c-1,c+2):
                # print("cs "+str(cs))
                try:
                    neighbour = pocket_dimension[zs][rs][cs]
                    if neighbour == 1:
                        activeNeighbours+=1
                    elif neighbour == 0:
                        inactiveNeighbours +=1
                except:
                    # print("nothing there")
                    pass
    print(activeNeighbours)
    print(inactiveNeighbours)
    try:
        actualVal = pocket_dimension[z][r][c]
        print("actualValue: " + str(actualVal))
    except:
        print("newValue: " + str(0))
        return 0
    if actualVal ==1 and ( activeNeighbours == 2 or activeNeighbours == 3):
        print("newValue: " + str(1))
        return 1 
    elif actualVal ==1:
        print("newValue: " + str(0))
        return 0
    elif actualVal == 0 and inactiveNeighbours == 3:
        print("newValue: " + str(1))
        return 1
    else:
        print("newValue: " + str(0))
        return 0
    print(inactiveNeighbours)
    print(activeNeighbours)

count=0
for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    temp = []
    for char in cleanLine:
        if char == ".":
            temp.append(0)
        elif char == "#":
            temp.append(1)
    
    pocket_dimension[1].append(temp)
    print(cleanLine)
    count+=1

print(pocket_dimension)

#6 rounds
# for i in range(6):

# checkPositioin(0,0,0)
temp_dimension = []
temp_dimension = pocket_dimension
print(temp_dimension)
for z in range(len(pocket_dimension)):
        # print("zs "+str(zs))
        for r in range(len(pocket_dimension[z])):
            # print("rs "+str(rs))
            for c in range(len(pocket_dimension[z][r])):
                temp_dimension[z][r][c] = checkPositioin(z,r,c)
                # print(pocket_dimension[z][r][z])
print(pocket_dimension)
print(temp_dimension)


print("--- %s seconds ---" % (time.time() - startTime))