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
    string = take_string()
    count = 0
    for i in range(len(string)):
        count = max(len(set(string[:i]))+len(set(string[i:])),count)
    print(count)
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
