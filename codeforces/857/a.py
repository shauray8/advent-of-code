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
    li = take_int_list()

    max_list = sorted(li,reverse=True)
    maxi = [0]
    mini = [0]
    buffer_state = []
    min_list = {}

    for i in range(len(max_list)):
        if abs(li[i]) in min_list:
            min_list[abs(li[i])] += 1
        else:
            min_list[abs(li[i])] = 1
        if -max_list[i] in buffer_state:
            maxi.append(maxi[-1]-1)
        else:
            buffer_state.append(max_list[i])
            maxi.append(maxi[-1]+1)

    minimum = sorted(min_list.items(), key=lambda x:x[1], reverse=True)

    for i in minimum:
        if i[1] == 2:
            mini.append(1)
            mini.append(0)

        else:
            mini.append(mini[-1]+1)

    for i in maxi[1:]:
        print(i,end = " ")

    print("")
    for i in mini[1:]:
        print(i,end = " ")
    print("")

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
