# Author: Shauray

import sys
input = sys.stdin.readline

def take_int():
    return(int(input()))
def take_list():
    return(list(map(int,input().split())))
def take_string():
    s = input()
    return(list(s[:len(s) - 1]))
def take_int_list():
    return(list(map(int,input().split())))

def solve(n):
    if sorted(set(n)) == sorted(n):
        return "".join(n)
    result = ""
    ctr = 1
    for i in range(len(n)):
        if i+1<len(n) and n[i] == n[i+1]:
            ctr+=1
        else:
            result += n[i]
            if ctr>1 or (result[ctr-1]<="9" or result[ctr-1]>="1"):
                result += str(ctr)
            ctr=1
    return result


if __name__ == "__main__":
    n = take_string()
    n = solve(n)
    print(n)

