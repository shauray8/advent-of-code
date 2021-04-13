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
    x,y = a[i][:-2].split("-")
    xbool = a[i][-1] == b[i][int(x)]
    ybool = a[i][-1] == b[i][int(y)]
    if (xbool and not ybool) or (ybool and not xbool):
        final += 1
        
print(final)
