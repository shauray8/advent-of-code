start = [10,12,20]
end = [20,25,30]
array = []

for i in range(len(start)):
    array.append([end[i],start[i],i])

array = sorted(array)
meetings = 1
limit = array[0][0]


for i in (array[1:]):
    if i[1] > limit:
        meetings += 1
        limit = i[0]

print(meetings)

## choose the shortest period for the meeting in that way the room stays less occupied !



