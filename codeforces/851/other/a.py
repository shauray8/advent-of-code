# Author: Shauray

from math import prod
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
    li = take_int_list()
    for i in range(len(li)):
        if li[:i].count(2) == li[i:].count(2):
            print(i)
            return
    print(-1)
    return 

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
