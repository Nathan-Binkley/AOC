import json
import re
import threading
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

instructions = []
for i, v in enumerate(vals):
    ins, inc = v.split()
    instructions.append([ins,inc])

acc = 0
done = False
counter = 0 
cList = []
mockList = []
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
    instructions.append([ins,inc])
# print(instructions)
acce = 0
done = False
counters = 0 
cList = []
lineList = []

def doTask(list):
    counter = 0
    acc = 0
    broken = False
    while counter < len(instructions):
        line = counter + 1 
        
        if line in lineList:
            broken = True
            break
        
        if instructions[counter][0] == 'acc':
            if instructions[counter][1][0] == "+":
                acc += int(instructions[counter][1][1:])
                counter += 1
            elif instructions[counter][1][0] == "-":
                acc -= int(instructions[counter][1][1:])
                counter += 1
        elif instructions[counter][0] == 'jmp':
            if instructions[counter][1][0] == "+":
                lineList.append(line)
                counter += int(instructions[counter][1][1:])
            elif instructions[counter][1][0] == "-":
                lineList.append(line)
                counter -= int(instructions[counter][1][1:])
        else:
            counter += 1
    if not broken:
        print(acc)

count = 0
List = []
for i in range(len(instructions)):
    if instructions[i][0] == 'jmp':
        ex = instructions[:]
        ex[i][0] = 'nop'
        List.append(i+1)
        doTask(ex)
        count += 1
    
# print(count)
# print(List)