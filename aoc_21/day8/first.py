import os
import statistics as s
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

count = 0

for i in range(len(lis)):
    _,out = lis[i].split("|")
    for j in out.split(" "):
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            count += 1


print(count)



    
            
                





