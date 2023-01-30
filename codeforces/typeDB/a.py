from math import log

def solve():
    for i in range(1,int(x)+2):
        for j in range(i,int(x)+2):
            if log(((i**j)*j) + ((j**i)*i)) == x:
                print(i,j)
                return
    print(-1)
    return

if __name__ == "__main__":
    n = int(input())
    while(n):
        x = int(input())
        if x%2 != 0:
            x = log(x)
            solve()
        else:
            print(1,x//2)
        n-=1
