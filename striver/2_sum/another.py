matrix = [2,7,11,15]
target = 9
hash_map = {}

def some():
    for i,num in enumerate(matrix):
        if target-num in hash_map:
            return [hash_map[target - num],i]
        hash_map[num] = i

print(some())


