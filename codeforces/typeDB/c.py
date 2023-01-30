
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

INF = 123456789

def solve():
    array = []
    for x1 in range(s,i+1):
        for x2 in range(s,i+1):
            if x1 + x2 == i:
                array.append([x1,x2])
    global_array.append(max(array))
    return

if __name__ == "__main__":
    x = take_int()
    while(x):
        n,s = take_int_list()
        li = take_int_list()
        global_array = []
        for i in li[1:n-1]:
            solve()
        print(global_array)
        f = li[0] * global_array[0][0] + li[-1] * global_array[-1][1]
        for i,j in zip(global_array[0:],global_array[1:]):
            f += i[1]*j[0]
        print(f)
        x-=1
