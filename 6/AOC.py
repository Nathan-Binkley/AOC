import json
import re
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

count = 'qwertyuiopasdfghjklzxcvbnm'
ans = 0
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
groups = []
group = []
for i in vals:
    if i != "":
        group.append(i)
    else:
        groups.append(group)
        group = []
for group in groups:
    inter = count[::]
    for person in group:
        inter = intersection(inter,person)
    ans += len(inter)
print(ans)