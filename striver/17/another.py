m,n = 3,7
c_count = []
dummy = [[-1]*(m+1)]*(n+1)
print(dummy)

def move(tracker,dummy):
    i,j = tracker[0],tracker[1]
    if tracker == [m-1,n-1]:
        c_count.append(1)
        return 1
    if tracker[0] >= m or tracker[1] >= n:
        return 0
    if dummy[i][j] != -1:
        c_count.append(dummy[i][j])
        return dummy[i][j]

    dummy[i][j] = move([i+1,j],dummy) + move([i,j+1], dummy)


move([0,0], dummy)
print(len(c_count))


