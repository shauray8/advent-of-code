#include <bits/stdc++.h>
using namespace std;

const long long INF = 9223372036854775807;

void solve(){
  int x;
  scanf("%d",&x);
  int alice = 1,bob = 0;
  int ll = 2;
  x -= 1;
  while(x){
    for(int i=0; i<2; i++){
      if(ll >= x){
        bob+=x;
        x = 0;
        break;
      }
      else{
        bob+=ll;
        x-=ll;
        ll++;
      }
    }
    for(int i=0; i<2; i++){
      if(ll >= x){
        alice+=x;
        x = 0;
        break;
      }
      else{
        alice+=ll;
        x-=ll;
        ll++;
      }
    }
  }
  printf("%d %d \n",alice,bob);
}

int main(){
  ios_base::sync_with_stdio(0);
  //cin.tie(0);

  int n;
  scanf("%d",&n);
  while(n--){
    solve();
  }
}
