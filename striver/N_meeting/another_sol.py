start = [10,12,20]
end = [20,25,30]
array = []

visited = [1]

for i in range(len(start)):
    array.append([end[i],start[i],i])

for i in sorted(array):
    
print(sorted(array))

for i in range(1, len(start)):
    if start[i] > end[visited[-1]-1]:
        visited.append(i+1)

print(visited)
