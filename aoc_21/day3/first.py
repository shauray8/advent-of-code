import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

epsilon = ""
gamma = ""
for j in range(len(lis[0])):
    ones, zeros = [], []
    for i in range(len(lis)):
        if int(lis[i][j]) == 1:
            ones.append(1)
        else:
            zeros.append(0)
    print(len(ones))
    print(len(zeros))

    if len(ones) > len(zeros):
        gamma += str(1)
    else:
        gamma += str(0)

    if len(ones) < len(zeros):
        epsilon += str(1)
    else:
        epsilon += str(0)



print(epsilon, gamma)

