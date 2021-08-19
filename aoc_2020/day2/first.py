lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
a,b = [],[]

for i in lis:
    first, second = i.split(":")
    a.append(first)
    b.append(second)

final = 0
for i in range(len(a)):
    best = 0
    
    for k in range(len(b[i])):
        if a[i][-1] == b[i][k]:
            best +=1
        x,y = a[i][:-2].split("-")
    if best in range(int(x),int(y)+1):
        final += 1

print(final)
