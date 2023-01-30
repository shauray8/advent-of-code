matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

## first method
def first(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix)):
                    if matrix[k][j] != 0:
                        matrix[k][j] = "-1"
                for k in range(len(matrix[0])):
                    if matrix[i][k] != 0:
                        matrix[i][k] = "-1"

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "-1":
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


def third(matrix):
    col0 = 1
    for i in range(len(matrix)):
        if matrix[i][0] == 0 : col0 = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)-1,0,-1):
        for j in range(len(matrix[0])-1,0,-1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                print(i,j)
                matrix[i][j] = 0

        if col0 == 0:
            print(i)
            matrix[i][0] = 0

    print(matrix)


third(matrix)



            
