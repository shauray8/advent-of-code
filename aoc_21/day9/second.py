import os
import statistics as s
import math
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split(",")

for i in range(len(lis)):
    lis[i] = int(lis[i])

mean = math.floor((s.mean(lis)))
count = 0
j = 1
while( lis.count(mean) != len(lis)):
    for i in range(len(lis)):
        if lis[i] > mean:
            count += j
            lis[i] = lis[i] - 1
        elif lis[i] < mean:
            count += j
            lis[i] = lis[i] + 1
        else:
            pass
    j += 1

print(count)
