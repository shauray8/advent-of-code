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
    length = take_int()
    string = take_string()
    pos1,pos2 = 0,0
    dic = {"U":[1,0],"L":[0,-1],"R":[0,1], "D":[-1,0]}
    for i in string:
        pos1 += dic[i][0]
        pos2 += dic[i][1]
        if pos1 == 1 and pos2 == 1:
            print("YES")
            return
    print("NO")
    return
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        solve()
        n-=1
