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
    x = take_int_list()
    main_list = take_int_list()
    for j in range(x[1]):
        i = take_int_list()
        total_sum = sum(main_list[:i[0]-1]+main_list[i[1]:])+(i[1]-i[0]+1)*i[2]
        if total_sum % 2 != 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
