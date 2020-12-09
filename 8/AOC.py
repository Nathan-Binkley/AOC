import json
import re
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

instructions = []
for i, v in enumerate(vals):
    ins, inc = v.split()
    instructions.append([ins,inc,0])
# print(instructions)
acc = 0
done = False
counter = 0 
cList = []
lineList = []
while not done:
    # cList.append(counter)
    if instructions[counter][2] == 1 or counter in cList:
        print(counter)
        print(lineList)
        done = True
    elif instructions[counter][0] == 'acc':
        if instructions[counter][1][0] == "+":
            acc += int(instructions[counter][1][1:])
            cList.append(counter)
            lineList.append(counter+1)
            counter += 1
        elif instructions[counter][1][0] == "-":
            acc -= int(instructions[counter][1][1:])
            cList.append(counter)
            lineList.append(counter+1)
            counter += 1
        instructions[counter][2] == 1
    elif instructions[counter][0] == 'jmp':
        if instructions[counter][1][0] == "+":
            cList.append(counter)
            lineList.append(counter+1)
            counter += int(instructions[counter][1][1:])
        elif instructions[counter][1][0] == "-":
            cList.append(counter)
            lineList.append(counter+1)
            counter -= int(instructions[counter][1][1:])
        instructions[counter][2] == 1
    else:
        instructions[counter][2] == 1
        cList.append(counter)
        lineList.append(counter+1)
        counter += 1
        
    
    # instructions[counter][2] == 1
    

print(acc)