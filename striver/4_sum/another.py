matrix = [4,3,3,4,4,2,1,2,1,1]
target = 9
hash_map = set()

def first():

    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            for k in range(j+1,len(matrix)):
                x = target - matrix[i] - matrix[j] - matrix[k]
                if x in matrix[k+1:]:
                    v = tuple(sorted([matrix[i], matrix[j], matrix[k], x]))
                    hash_map.add(v)


def second():
    sorted(matrix)
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            x = target - matrix[i] - matrix[j]
            start = j+1
            end = len(matrix)-1
            while start < end:
                two_sum = matrix[start] + matrix[end]
                if two_sum<x: start += 1
                elif two_sum > x: end -= 1
                else:   
                    v = tuple(sorted([matrix[i], matrix[j], matrix[start], matrix[end]]))
                    hash_map.add(v)
                    while start < end and matrix[start] == v[2]: start += 1
                    
                    while start < end and matrix[end] == v[3]: end -= 1
            while j + 1 < len(matrix) and matrix[j + 1] == matrix[j]: j+=1;

        while i + 1 < len(matrix) and matrix[i + 1] == matrix[i]: i+=1;
                
                    
second()

print([list(maps) for maps in hash_map])

