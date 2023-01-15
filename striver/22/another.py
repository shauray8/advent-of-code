matrix = [6, -2, 2, -8, 1, 7, 4, -10]

alpha = 0
for i in range(len(matrix)):
    sigma = 0
    for j in range(i, len(matrix)):
        sigma += matrix[j]
        if sigma == 0:
            alpha = max(alpha, j-i+1)

print(alpha)
