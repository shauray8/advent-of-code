import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n\n")

numbers = []
for i in lis[0].split(","):
    numbers.append(i)
a = []
for k in numbers:
    for i in range(1,len(lis)):
        for j in range(len(lis[i].split())):
            #a.append(lis[i].split())
            if k == lis[i].split()[j] :
                lis[i].split()[j] = "x"
                a.append((i,j))


            #print(lis[i].split()[j][0:5])
    a = sorted(a)
    gg = []
    for i in range(len(a)-1):
        if a[i][0] == a[i+1][0]:
            gg.append(a[i][1]))
        else:
            for i in gg:



    
            
                





