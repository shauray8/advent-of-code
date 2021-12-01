import os
fn =  "data.txt"
lis = open(fn).read().strip().split("\n")

inc = 0
dec = 0
arr = []
for i in range(0,len(lis)-2):
    sum1 = 0
    for j in range(3):
        sum1 += (int(lis[i+j]))
    arr.append(sum1)

for i in range(len(arr)-1):
    if int(arr[i]) > int(arr[i+1]):
        dec += 1
    elif int(arr[i]) == int(arr[i+1]):
        pass
    else:
        inc += 1

print(inc)




