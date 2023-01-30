import math
x = int(input())
counts = []
while(x):
    count = []
    a,s,r = str(input()).split(" ")
    a,s,r = int(a),int(s),int(r)
    n = a
    n = n-1
    count.append(s-r)
    while n:
        if math.ceil(r/n) <=6 and r-math.ceil(r/n) >= 0:
            count.append(math.ceil(r/n))
            r -= math.ceil(r/n)
        else:
            count.append(r-math.ceil(r/n))
            r -= r-math.ceil(r/n)
        n-=1
    counts.append(count)
    x -= 1


for i in counts:
    for j in i:
        print(j,end=' ')
    print("")
