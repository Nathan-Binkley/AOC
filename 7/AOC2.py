import json
import re
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)
bags = {}

for i in vals:
    bag, contents = i.split("contain")
    bags.setdefault(bag.replace('bags','').replace('bag','').rstrip().lstrip(),[])
    contents = contents.split(',')
    for j in contents:
        j = j.rstrip().lstrip()
        num, j = j.split(" ",1)
        j = j.replace('.','')
        j = j.replace('bags','')
        j = j.replace('bag','')
        bags[bag.replace('bags','').replace('bag','').rstrip().lstrip()].append([num, j.rstrip().lstrip()])

with open('output.json','w') as f:
    json.dump( bags,f, indent=4)
# print(bags)

def findCount(b):
    count = 1
    for bag in b:
        if 'no' in bag[0]:
            count = 1
        else:
            count += int(bag[0]) * findCount(bags[bag[1]])
    return count

print(findCount(bags['shiny gold'])-1) #exclude bag you start with