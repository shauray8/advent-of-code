import os

lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")

for i in range(len(lis)-1):
    for j in range(len(lis)-1):
        if int(lis[i]) + int(lis[j]) == 2020:
            a = int(lis[i])*int(lis[j])
            break
print(a)
