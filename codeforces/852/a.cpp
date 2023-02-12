#include <bits/stdc++.h>
using namespace std;

const long long INF = 9223372036854775807;
#define ll long long

void solve(){
  ll a,b,n,m;
  scanf("%lld %lld",&a,&b);
  scanf("%lld %lld",&n,&m);
  ll local = INF;
  auto pass = 0;
  for(ll i=0; i<=n; i++){
    if (i % m == 0 && i != 0){
      if((n-i-pass) > 0){
        pass += 1;
        local = min((long long)(i*a + (n-i-pass)*b),local);
      }
    }
    else{
      if((n-i-pass) >= 0){
        local = min((long long)(i*a + (n-i-pass)*b),local);
      }
    }
  }
  printf("%lld \n",local);
}

int main(){
  ios_base::sync_with_stdio(0);
  //cin.tie(0);

  int x;
  scanf("%d",&x);
  while(x--){
    solve();
  }
}
