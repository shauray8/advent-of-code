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
    some = take_int_list()
    global_max = -10**5
    for i in range(len(some)-1):
        some[i], some[i+1] = -some[i],-some[i+1]
        global_max = max(sum(some), global_max)
        if some[i] ==1 and some[i+1] == 1:
            break
        some[i], some[i+1] = -some[i],-some[i+1]
    print(global_max)
    return

if __name__ == "__main__":
    n = take_int()
    while(n):
        x = take_int()
        solve()
        n-=1

