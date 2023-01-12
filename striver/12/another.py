array = [5,3,2,1,4]

count = 0
for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i] > array[j]:
            array[i],array[j] = array[j],array[i]
            count += 1
print(count)
