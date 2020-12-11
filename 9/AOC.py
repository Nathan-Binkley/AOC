import json
import re
import time
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(int(l))

before = []
answers = []

def FindPairs(arr, k):
    master = []
    for v1 in arr:
        for v2 in arr:
            master.append(v1 + v2)
    if k not in master:
        # print(sorted(master))
        return True

for num in range(25, len(vals)):
    before = vals[num-25:num]
    startLine = num-24
    endLine = num
    diff = endLine-startLine
    currVal = vals[num]

    if FindPairs(before, vals[num]):
        pt1 = vals[num]
        # print(before)
        break

print("PT 1 ANSWER: " + str(pt1))


# PT 2
for i in range(len(vals)):
    for j in range(i, len(vals)):
        if sum(vals[i:j]) == pt1:
            print(vals[i:j])
            ma = max(vals[i:j])
            mi = min(vals[i:j])
            print(ma + mi)

    
    

# print(answers)
# print(before)

# WORKS FOR PT 1
# ANS: 10884537
# def FindPairs(arr, k):
#     master = []
#     for v1 in arr:
#         for v2 in arr:
#             master.append(v1 + v2)
#     if k not in master:
#         print(sorted(master))
#         return True
        
#     return False
# for num in range(25, len(vals)):
#     before = vals[num-25:num]
#     startLine = num-24
#     endLine = num
#     diff = endLine-startLine
#     currVal = vals[num]

#     if FindPairs(before, vals[num]):
#         print(vals[num])
#         # print(before)
#         break
    
#     print()
    