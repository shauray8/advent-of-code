x = int(input())
counts = []
pi = "314159265358979323846264338327"
while(x):
    a = str(input())
    count = 0
    for i in range(len(a)):
        if a[i] == pi[i]:
            count += 1
        else:
            break
    counts.append(count)
    x -= 1

for i in counts:
    print(i)
