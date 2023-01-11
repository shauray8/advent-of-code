entries = sorted([[1,4],[4,5]])
another = []
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

print(final)


