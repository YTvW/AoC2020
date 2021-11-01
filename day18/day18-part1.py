import sys
import fileinput
from re import search
import time
startTime = time.time()
expressionList = []
# for line in fileinput.input("./input.txt"):
for line in fileinput.input("./test.txt"):
    cleanLine = line.encode("utf-8").strip("\n").replace(" ","")
    expressionList.append(cleanLine)
    # print(cleanLine)

def doCmd(prev, inp, cmd):
    if cmd == "*":
        return prev * inp
    elif cmd == "+":
        return prev + inp
    elif cmd == "-":
        return prev - inp

def parseBlock(arr):
    res = 0
    temp = 0
    offset = 0
    lvl = 0
    cmd = ""
    cr =0
    while cr < len(arr):
        char = arr[cr]
        if char.isdigit():
            if cmd != "":
                res = doCmd(res,int(char),cmd)
                cmd = ""
            elif res == 0:
                res = int(char)
        elif char.count("("):

            count,temp2 = parseBlock(arr[cr+1::])
            cr += count
            offset +=count
            if cmd != "":
                res = doCmd(res,temp2,cmd)
                cmd = ""
            elif res == 0:
                res = temp2
        elif char.count(")"):
            offset +=1
            return offset,res
            break
        elif char.count("+") == 1:
            cmd = char
        elif char.count("*") == 1:
            cmd = char
        offset +=1
        cr +=1
    return offset, res

total = 0
for exp in expressionList:
    offset, res = parseBlock(exp)
    total+=res

print("result: " + str(total))
print("--- %s seconds ---" % (time.time() - startTime))