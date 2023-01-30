array = [3,1,2,5,4,6,7,5]
freq = [0]*(len(array)+1)

for i in range(len(array)):
    freq[array[i]] += 1

a = []
for i in range(1,len(freq)):
    if freq[i] == 0 or freq[i] > 1:
        a.append(i)

print(a)
