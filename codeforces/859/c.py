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
    word = "".join(word)
    word = word.replace(word[0],"1")
    for i in range(1,len(word)):
        if i % 2 == 0 and (word[i] != "0" or word[i] != "1"):
            word = word.replace(word[i],"1")
            if word[i-1] == word[i]:
                print("NO")
                return
        elif i % 2 != 0 and (word[i] != "0" or word[i] != "1"):
            word = word.replace(word[i],"0")
            if word[i-1] == word[i]:
                print("NO")
                return
        else:
            pass

    ans = "YES"
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            ans = "YES"
        else:
            ans = "NO"
            break
    print(ans)
    return

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
