import os
import statistics as s
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split(",")

for i in range(len(lis)):
    lis[i] = int(lis[i])

s.mean(lis)
count = 0
while(s.mean(lis) == )
for i in range(len(lis)):
    if lis[i] > s.median(lis):
        count += abs(lis[i] - int(s.median(lis)))
        lis[i] = lis[i] - abs(lis[i] - int(s.median(lis)))
    elif lis[i] < s.median(lis):
        count += abs(lis[i] - int(s.median(lis)))
        lis[i] = lis[i] + abs(lis[i] - int(s.median(lis)))

    else:
        pass

print(lis)
print(count)



    
            
                





