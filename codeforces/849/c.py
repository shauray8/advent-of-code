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
    bina = take_string()
    some = len(bina)
    for i,j in zip(bina, bina[::-1]):
        if i != j:
            some-=2
            if some == 0:
                print(some)
                return
        else:
            print(some)
            return
    return

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
