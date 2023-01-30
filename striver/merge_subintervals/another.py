entries = sorted([[1,3],[2,6],[8,10],[15,18]])
another = []

def brute():
    intervals = sorted(intervals)
    for i in range(len(intervals)):
        start,end = intervals[i][0], intervals[i][1]
        if (len(another) != 0):
            if start <= another[-1][1]:
                continue
                        
        for j in range(i+1, len(intervals)):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])

        end = max(end, intervals[i][1])
        another.append([start, end])

another.append(entries[0])
for i in range(1,len(entries)):
    if entries[i][0] <= another[-1][1]:
        another[-1][1] = max(another[-1][1],entries[i][1])]
    else:
        another.append(entries[i])


print(another)


