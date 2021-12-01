import os
lis = []
w = open('day1_data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis = lis[:-1]
inc = 0
print(lis)
dec = 0
for i in range(0,len(lis)-1):
    if int(lis[i]) - int(lis[i+1]) > 0:
        dec += 1
    else:
        inc += 1


print(inc)
print(dec)
print(len(lis))

