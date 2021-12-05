import os
import numpy as np
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")
zeros = np.zeros([1000,1000])
print(zeros.shape)
for i in range(len(lis)):
    x,y = lis[i].split("->")
    x1,y1 = x.strip().split(",")
    x2,y2 = y.strip().split(",")
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)

    if y1 == y2:
        print(x1,x2,y1,y2)
        if x1>x2:
            for i in range(abs(x1-x2)+1):
                zeros[x1-i][y1] += 1
        if x1<x2:
            for i in range(abs(x1-x2)+1):
                zeros[x1+i][y1] += 1
    elif x1 == x2:
        if y1>y2:
            for i in range(abs(y1-y2)+1):
                zeros[x1][y1-i] += 1
        if y1<y2:
            for i in range(abs(y1-y2)+1):
                zeros[x1][y1+i] += 1
    else:
        print(x1,x2,y1,y2)
        if x1 > x2 and y1 < y2:
            for i in range(abs(x1-x2)+1):
                zeros[x1-i][y1+i] += 1
        if x1 < x2 and y1 > y2:
            for i in range(abs(x1-x2)+1):
                zeros[x1+i][y1-i] += 1
        if x1 > x2 and y1 > y2:
            for i in range(abs(x1-x2)+1):
                zeros[x1-i][y1-i] += 1
        if x1 < x2 and y1 < y2:
            for i in range(abs(x1-x2)+1):
                zeros[x1+i][y1+i] += 1

count = 0
for i in zeros:
    for j in i:
        if j >= 2.:
            count += 1

print(count)
    


    
            
                








