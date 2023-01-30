import sys

alpha = "abcdefghijklmn"
print(f"{sys.argv[2]} files created with extention {sys.argv[1]}")
if sys.argv[1] == "py":
    for i in range(int(sys.argv[2])):
        filename = f"{sys.argv[3]}/{alpha[i]}.{sys.argv[1]}"
        with open(filename,'w') as fp:
            fp.write(
"""import sys
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
    pass

if __name__ == "__main__":
    n = take_int()
    while(n):
        n-=1
""")
            pass

if sys.argv[1] == "cpp":
    for i in range(int(sys.argv[2])):
        filename = f"{sys.argv[3]}/{alpha[i]}.{sys.argv[1]}"
        with open(filename,'w') as fp:
            fp.write(
"""#include <bits/stdc++.h>
using namespace std;

const long long INF = 9223372036854775807;
#define ll long long

void solve(){
  ;
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n;
  scanf("%d",n);
  while(n--){
    solve();
  }
}
""")
            pass

