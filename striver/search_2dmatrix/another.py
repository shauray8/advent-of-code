matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
n = 3
def find():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if n == matrix[i][j]:
                return True

print(find())
