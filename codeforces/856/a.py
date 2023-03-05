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
def take_string_list():
    return(list(map(str,input().split())))

def solve():
    x = take_int()
    li = take_string_list()
    for i in range(len(li)):
        li[i] = "".join(sorted(li[i]))

    buf = {}
    for i in li:
        if i in buf:
            buf[i] += 1
        else:
            buf[i] = 1

    for i in buf.items():
        if i[1] % 2 != 0:
            print("NO")
            return 
    print("YES")
    return


if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
