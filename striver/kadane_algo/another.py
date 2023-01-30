import sys
matrix = [-2,1,-3,4,-1,2,1,-5,4]


def OofN3():
    max_ans = sys.minint
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            ans = 0
            for k in range(i,j):
                ans += matrix[k]
            if ans > max_ans:
                max_ans = ans

def OofN2():
    max_ans = sys.minint
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            ans = sum(matrix[i:j])
            if ans > max_ans:
                max_ans = ans

def optimal(matrix):
    msf = -10**4
    meh = 0
    s = 0
    dummy = []
    for i in range(len(matrix)):
        meh += matrix[i]
        if meh > msf:
            dummy = []
            msf = meh
            dummy.append(s)
            dummy.append(i)

        if meh < 0:
            meh = 0;
            s = i+1


    return msf, dummy

print(optimal(matrix))
