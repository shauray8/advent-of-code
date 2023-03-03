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
    operations = take_int_list()
    word = take_string()
    buffer = {}
    for i in word:
        if i in buffer:
            buffer[i] += 1
        else:
            buffer[i] = 1

    store = 0
    another_store = 0
    for i in buffer.items():
        if i[0] == i[0].lower():
            upper = buffer[i[0].upper()] if i[0].upper() in buffer else 0
            store += abs(upper - buffer[i[0]]) // 2
            another_store += min(upper,buffer[i[0]])

        if i[0].lower() not in buffer:
            upper = 0
            store += abs(upper - buffer[i[0]]) // 2
            another_store += min(upper,buffer[i[0]])


    print(another_store + min(store,operations[1]))
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
