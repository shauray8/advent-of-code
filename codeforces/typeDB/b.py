
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
    return(map(int,input().split()))

global_array = []

def _factors():
   for i in range(1, x + 1):
       if x % i == 0:
           global_array.append(i)

def solve():
    print(global_array)
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        x = take_int()
        _factors()
        solve()
        n-=1
