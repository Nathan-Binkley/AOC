import json
import re
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
string = ""
e = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for line in vals:
    if line != "": 
        string += line + " "
    else: #signifies end of a passport
        count = 0
        functions = string.split()
        indices = [functions.pop(i) for i, s in enumerate(functions) if 'cid' in s]
        for i in functions:
            if len(functions) == 7 or len(functions) == 8:
                attr = i.split(":")
                if(attr[0] == "byr"): 
                    if (int(attr[1]) >= 1920 and int(attr[1]) <= 2002):
                        count += 1
                elif(attr[0] == "iyr"): 
                    if (int(attr[1]) >= 2010 and int(attr[1]) <= 2020):
                        count += 1
                elif(attr[0] == "eyr"):
                    if (int(attr[1]) >= 2020 and int(attr[1]) <= 2030):
                        count += 1
                elif(attr[0] == "hgt" and "cm" in attr[1]):
                    if (int(attr[1][:-2]) >= 150 and int(attr[1][:-2]) <= 193):   
                        count += 1
                elif(attr[0] == "hgt" and "in" in attr[1]):
                    if (int(attr[1][:-2]) >= 59 and int(attr[1][:-2]) <= 76):   
                        count += 1
                elif(attr[0] == "hcl"):
                    match = re.search(r'^#(?:[0-9a-f]{3}){1,2}$', attr[1])   
                    if match:
                        count += 1             
                elif(attr[0] == "ecl"):
                    if(attr[1] in e):  
                        count += 1
                elif (attr[0] == 'pid'):
                    if( len(attr[1]) == 9):
                        count += 1
                if count == 7:
                    valid += 1
        string = ""
print(valid)