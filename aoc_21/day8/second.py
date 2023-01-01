import os
import statistics as s
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

count = 0

for i in range(len(lis)):
    _,out = lis[i].split("|")
    ff = {}
    for j in _.split(" "):
        if len(j) == 2:
            ff[1] = j[0]
            ff[2] = j[1]
        elif len(j) == 4:
        elif len(j) == 3:
            ff[6] = j[0]
            ff[1] = j[1]
            ff[2] = j[2]
        elif len(j) == 7:
            

            


print(count)
