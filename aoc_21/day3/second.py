import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

forward, depth, aim = 0,0,0

for i in lis:
    op, nu = i.split(" ")
    if op == "forward":
        forward += int(nu)
        depth += aim*int(nu)
    elif op == "down":
        aim += int(nu)
    else: 
        aim -= int(nu)


print(forward*depth)


