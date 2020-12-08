import sys
import fileinput
from re import search
import time
startTime = time.time()
passport = []
count = 0
validCount = 0
seemingly_valid= []

# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.

requirements = {
"byr": 0,
"iyr" : 0,
"eyr" : 0 ,
"hgt" : "",
"hcl" : "",
"ecl" : 0,
"pid" : "",


}
def findEntry(passport, entry):
    for item in passport:
        if entry in item:
            return item

def check_byr(byr):
    if int(byr) <= 2002 and int(byr) >= 1920:
        return True
    else:
        return False

def check_iyr(iyr):
    if int(iyr) <= 2020 and int(iyr) >= 2010:
        return True
    else:
        return False

def check_eyr(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return True
    else:
        return False

def check_hgt(hgt):
    match= search("^([0-9]{0,3})(cm|in)$",hgt)
    if match == None:
        # print("NoMatch")
        return False
    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    if match.group(2) == "cm":
        # print("CM")
        if int(match.group(1)) <= 193 and int(match.group(1)) >= 150:
            return True
        else:
            return False
    elif match.group(2) == "in":
        # print("IN")
        if int(match.group(1)) <= 76 and int(match.group(1)) >= 59:
            return True
        else:
            return False
    else:
        return False

def check_hcl(hcl):
    match = search("^#{1}([0-9a-f]{6}|[0-9a-f]{3})$",hcl)
    if match == None:
        return False
    else:
        return True

def check_ecl(ecl):
    colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if colours.count(ecl) == 1:
        return True
    else:
        return False

def check_pid(pid):
    match = search("^([0-9]{9})$", pid)
    if match == None:
        return False
    else:
        return True

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# data = fileinput.FileInput("./input.txt")
lastLine= None
for line in fileinput.input("./input.txt"):
    if line == "\n":
        count += 1
        if len(passport) >= 7:
            if len(passport) == 8:
                validCount +=1
                seemingly_valid.append(passport)
            else:
                cidFound =False
                for entry in passport:
                    if "cid" in entry:
                        cidFound = True
                        # print("found cid so invalid")
                        break
                if not cidFound:
                    validCount +=1
                    seemingly_valid.append(passport)
        
        passport = []
    if line != "\n":
        passport.extend(line.encode("utf-8").strip("\n").split(" "))

goodCount = 0
badCount = 0
for passport in seemingly_valid:
    byr = findEntry(passport,"byr").split(":")[1]
    iyr = findEntry(passport,"iyr").split(":")[1]
    eyr = findEntry(passport,"eyr").split(":")[1]
    hgt = findEntry(passport,"hgt").split(":")[1]
    hcl = findEntry(passport,"hcl").split(":")[1]
    ecl = findEntry(passport,"ecl").split(":")[1]
    pid = findEntry(passport,"pid").split(":")[1]
    # print("########")
    # print("byr: " + str(byr)+ " " + str(check_byr(byr)))
    # print("iyr: " + str(iyr) + " " + str(check_iyr(iyr)))
    # print("eyr: " + str(eyr) + " " + str(check_eyr(eyr)))
    # print("hgt: " + str(hgt) + " " + str(check_hgt(hgt)))
    # print("hcl: " + str(hcl) + " " + str(check_hcl(hcl)))
    # print("ecl: " + str(ecl) + " " + str(check_ecl(ecl)))
    # print("pid: " + str(pid) + " " + str(check_pid(pid)))
    # print("########")
    if (check_byr(byr) & check_iyr(iyr) & check_eyr(eyr) & check_hgt(hgt) & check_hcl(hcl) & check_ecl(ecl) & check_pid(pid)):
        goodCount +=1
    else:
        badCount += 1
        # print("@@@@@@@@@@@@@@@")
        # print(passport)
        # print("@@@@@@@@@@@@@@@")

print(badCount)
print(goodCount)
print(validCount)
print("--- %s seconds ---" % (time.time() - startTime))