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
    some = take_int_list()
    count = sum(some)
    for i in range(len(some)-1):
        some[i],some[i+1] = -some[i], -some[i+1]
        if count >= sum(some):
            count = max(sum(some),count)
            some[i],some[i+1] = -some[i], -some[i+1]
        else:
            count = max(sum(some),count)
    print(count)
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
