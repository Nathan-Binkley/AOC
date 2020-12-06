import json
import re
vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

minVal = 1
maxVal = 128 #max val
rows = []
cols = []
minCol = 0
maxCol = 7
seats = []
row = 0
column = 0
half = 0
    # for i in range(128):
    #     rows.append(i)
    # for i in range(8):
    #     cols.append(i)

    # for i in string:
    #     half = 0
    #     if i == 'F':
    #         half = len(rows)//2
    #         rows = rows[:half]
    #     elif i == 'B':
    #         half = (len(rows)+1)//2
    #         rows = rows[half:]
    #     if len(rows) == 1:
    #         row = rows[0]
    #     if i == 'R':
    #         half = (len(cols)+1)//2
    #         cols = cols[half:]
    #     elif i == 'L':
    #         half = len(cols)//2
    #         cols = cols[:half]
    #     if len(cols) == 1:
    #         column = cols[0]
for string in vals:
    minVal = 0
    maxVal = 127
    minCol = 0
    maxCol = 7

    
    # print(minVal)
    # print(maxVal)
    # print(minCol)
    # print(maxCol)
    # print()

    for i in string:
        
        if i == 'F':
            maxVal = (minVal+maxVal)//2
        elif i == 'B':
            minVal = (maxVal+minVal)//2
        if minVal == maxVal-1:
            row = minVal
            # print("FINAL ROW: ")
            # print(row)
        if i == 'R':
            minCol = (minCol+maxCol)//2 
        elif i == 'L':
            maxCol = (maxCol+minCol)//2
        if minCol == maxCol-1:
            column = maxCol 
            # print("FINAL COL: ")
            # print(column)
        # print()
    seats.append([row, column])
    # print([row,column])
    # print('------------')
answers = []
# for i in sorted(seats):
for row in range(128):
    for col in range(1,8):
        if [row, col] not in seats:
            answers.append([row,col])
    # if 
print(answers)

