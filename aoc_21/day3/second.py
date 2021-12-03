import os
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

epsilon = ""
gamma = ""
l = len(lis[0])

for j in range(l):
    ones, zeros = [], []
    oneh, zeroh = [], []

    for i in range(len(lis)):
        if int(lis[i][j]) == 1:
            ones.append(1)
            oneh.append(lis[i])
        else:
            zeros.append(0)
            zeroh.append(lis[i])
    print(len(ones))
    print(len(zeros))

    if len(ones) > len(zeros):
        lis = oneh
    else:
        lis = zeroh

    if len(lis) == 1:
        print("done")
    print(lis)

for j in range(l):
    ones, zeros = [], []
    oneh, zeroh = [], []

    for i in range(len(lis)):
        if int(lis[i][j]) == 1:
            ones.append(1)
            oneh.append(lis[i])
        else:
            zeros.append(0)
            zeroh.append(lis[i])
    print(len(ones))
    print(len(zeros))

    if len(ones) < len(zeros):
        lis = oneh
    else:
        lis = zeroh

    if len(lis) == 1:

        print(lis)
        break


