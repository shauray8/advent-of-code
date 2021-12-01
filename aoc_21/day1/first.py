import os
fn =  "data.txt"
lis = open(fn).read().strip().split("\n")

inc = 0
dec = 0
for i in range(0,len(lis)-1):
    if int(lis[i]) - int(lis[i+1]) > 0:
        dec += 1
    else:
        inc += 1

print(inc)
print(dec)
print(len(lis))

