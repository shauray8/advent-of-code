matrix = [3, 8, 5, 7, 6]

hash_set = set()

for i in range(len(matrix)):
    hash_set.add(matrix[i])

streak = 0
for i in range(len(matrix)):
    if matrix[i]-1 not in hash_set:
        curr = matrix[i]
        curr_streak = 1

        while curr+1 in hash_set:
            curr += 1
            curr_streak += 1

        streak = max(streak,curr_streak)

print(streak)

