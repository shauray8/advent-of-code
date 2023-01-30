matrix = [4, 2, 2, 6, 4]
target = 6
global_streak, local_streak = 0,0
hash_map = {}

for i in range(len(matrix)):
    local_streak ^= matrix[i]
    if local_streak == target:
        global_streak += 1 
    if local_streak^target in hash_map:
        global_streak += hash_map[local_streak^target]
    hash_map[local_streak] += 1

print(global_streak)
