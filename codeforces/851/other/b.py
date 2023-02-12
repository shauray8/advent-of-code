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

def solve():
    X = take_int()
    if X % 2 == 0:
        xx,yy = X//2, X//2
        print(xx,yy)
        return
    for i in range(10):
        xx = i
        yy = X-i
        if abs(sum([int(cx) for cx in str(xx)]) - sum([int(cx) for cx in str(yy)])) <= 1:
            print(yy,xx)
            return
    return

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
