arr = sorted([1,2,3,4,2,2])

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
        break


