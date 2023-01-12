arr1 = [1,4,8,10]
arr2 = [2,3,9]

arr_sort = []

arr_sort = sorted(arr1 + arr2)

for i in range(len(arr1)):
    arr1[i] = arr_sort[i]
for j in range(len(arr2)):
    arr2[j] = arr_sort[j+len(arr1)]


print(arr1, arr2)
