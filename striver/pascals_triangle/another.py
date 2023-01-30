matrix = [[1],[1,1],[1,2,1],[1,3,3,1]]
num = 5
another_matrix = [[0]]*num

for i in range(num):
    another_matrix[i] = [0]*(i+1)
    another_matrix[i][0],another_matrix[i][-1] = 1,1
    for j in range(1,i):
        another_matrix[i][j] = another_matrix[i-1][j-1] + another_matrix[i-1][j]


print(another_matrix)


