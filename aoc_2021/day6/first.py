import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split(",")
 
for i in range(256):
    for j in range(len(lis)):
        lis[j] = int(lis[j])
        if lis[j] == 0:
            lis[j] = 6
            lis.append(8) 
        else:
            lis[j] -= 1
print(len(lis))


    
            
                





