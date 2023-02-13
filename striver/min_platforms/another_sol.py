arr = ["9:00","9:45","9:55","11:00","15:00","18:00"]
dep = ["9:20","12:00","11:30","11:50","19:00","20:00"]

for i in range(len(arr)):
    arr[i] ="".join(arr[i].split(":"))
    dep[i] ="".join(dep[i].split(":"))

ans = 1
for i in range(len(arr)):
    count = 1
    for j in range(i,len(arr)):
        if (arr[i] >= arr[j] and arr[i]<=dep[j]) or (arr[j]>=arr[i] and arr[j]<=dep[i]):
            count+=1
    ans = max(ans,count)
print(ans)


