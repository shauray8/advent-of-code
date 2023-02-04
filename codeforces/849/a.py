
def solve():
    char = str(input())
    if char in "codeforces":
        print("YES")
        return
    print("NO")
    return

if __name__ == "__main__":
    n = int(input())
    while(n):
        solve()
        n-=1
