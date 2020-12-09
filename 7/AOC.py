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
        j = re.sub(" \d+", " ", j)
        j = j.replace('.','')
        j = j.replace('bags','')
        j = j.replace('bag','')
        bags[bag.replace('bags','').replace('bag','').rstrip().lstrip()].append(j.rstrip().lstrip())

with open('output.json','w') as f:
    json.dump( bags,f, indent=4)
containing = []
count = 0
def findGold(b):
    count = 0
    for bag in b:
        # print(bag)
        if bags[bag][0] == 'no other':
            pass
        else:
            if 'shiny gold' not in bags[bag]:
                if findGold(bags[bag]) > 0:
                    count += 1
            else:
                count += 1

    return count
# print(bags) 
print(findGold(bags))


# print(sorted(containing))
# print(len(containing))   
# print(bags)