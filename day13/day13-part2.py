import sys
import fileinput
from re import search
import time
startTime = time.time()
info = []
# for line in fileinput.input("./input.txt"):
for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    info.append(cleanLine)
    print(cleanLine)

busses = info[1].split(",")
print(busses)
closest = int(busses[-1])
bus = 0
t = 0
found = False

def checkBus(index):
    global t
    global busses
    # print("index: " + str(index))
    # print(busses[index])
    if busses[index] == "x":
        # print("don't care")
        return checkBus(index+1)
    print(t+index)
    if t+index % int(busses[index]) == 0:
        # print("nextLevel")
        return checkBus(index+1)
    else:
        # print("done")
        return False
    # return bool(t+offset % int(busses[index]) == 0)

# res = checkBus(0)
# print(res)
while not found:
#     # res = t % int(busses[0]) and t % int(busses[1])+
    if checkBus(1):
        print("lol")
        found = True
    t +=1
    time.sleep(1)
    # print(t)
# print(t)

# for bus in busses:
    # res = expectedTime % int(bus)
    # nextTime = expectedTime+ (int(bus)-res) 
    # waitTime = nextTime - expectedTime
    # if nextTime - expectedTime < closest:
    #     closest= waitTime
    #     bus = int(bus)
    # print(res)
    
print("result: " + str(closest*bus))
print("--- %s seconds ---" % (time.time() - startTime))