vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)
print(len(vals))

for i in vals:
    for j in vals:
        for k in vals:
            if int(i) + int(j) + int(k)== 2020:
                print(int(i) * int(j) * int(k))
    