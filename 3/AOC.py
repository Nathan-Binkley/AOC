vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)

trees = 0
horizontal = 0
try:
    for i, line in enumerate(vals):
        if line[horizontal % len(line)] == '#':
            trees += 1
        horizontal += 1
except:
    print(trees)