matrix = [[0,1,2,0],[3,4,5,2],[1,2,1,5]]

## first method
def first(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix)):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1
                for k in range(len(matrix[0])):
                    if matrix[i][k] != 0:
                        print(matrix[i][k])
                        matrix[i][k] = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix

def second(matrix):
    row = [1]*len(matrix)
    col = [1]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 0 or col[j] == 0:
                matrix[i][j] = 0;

    print(matrix)


second(matrix)



            
