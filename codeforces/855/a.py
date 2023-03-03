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
    another_word = "".join(word).lower()
    might = another_word[0]
    for i in range(1,len(another_word)):
        if another_word[i] != might[-1]:
            might += another_word[i]

    if might == "meow":
        print("YES")
        return
    print("NO")
    return

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
