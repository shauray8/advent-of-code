matrix = [1,3,2,3,1]

def merge(a,b):
    c = []
    a_idx, b_idx = 0,0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a): c.extend(b[b_idx:])
    else: c.extend(a[a_idx:])

    return c

def merge_sort(matrix):
    if len(matrix) <= 1: return matrix
    left, right = merge_sort(matrix[:len(matrix)//2]), merge_sort(matrix[len(matrix)//2:])
    return merge(left,right)

print(merge_sort(matrix))

