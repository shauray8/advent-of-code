matrix = [7,1,5,3,6,4]

def TLE():
    global_max = 0
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            local_max = matrix[j] - matrix[i]
            if local_max > global_max:
                global_max = local_max

global_max = 0
local_min = 10**4
for i in range(len(matrix)):
    local_min = min(local_min, matrix[i])
    global_max = max(-local_min+matrix[i], global_max)

print(global_max)

