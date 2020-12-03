vals = []
with open("input.txt", "r") as f:
    line = f.read()
    for l in line.split('\n'):
        vals.append(l)
count = 0
for i in vals:
    min_val, vals = i.split('-', 1)
    max_val = vals.split()[0]
    letter, password = vals.split(":")
    letter = letter[-1].strip()
    password = password.lstrip()
    if password[int(min_val)-1] == letter and password[int(max_val) - 1] == letter:
        
    elif password[int(min_val)-1] == letter or password[int(max_val) - 1] == letter:
        count += 1
print(count) #SHOULD BE 611