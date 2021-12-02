import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

forward, depth = 0,0

for i in lis:
    op, nu = i.split(" ")
    if op == "forward":
        forward += int(nu)
    elif op == "down":
        depth += int(nu)
    else: 
        depth -= int(nu)


print(forward*depth)

