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
    x = take_int()
    word = take_string()
    li = []
    word = "".join(word)
    for i in range(len(word)-1):
        if word[0:i]+word[i+2:] not in li:
            li.append(word[0:i]+word[i+2:])
    print(len(li))
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
