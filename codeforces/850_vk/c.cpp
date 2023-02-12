#include <bits/stdc++.h>
using namespace std;

#define ll long long


void solve(){
  long long counts = 0;
  int x;
  scanf("%d",&x);
  vector<int> monsters;
  while(x--){
    int m;
    scanf("%d",&m);
    monsters.push_back(m);
  }
  int curr = 1;
  sort(monsters.begin(), monsters.end());
  for(int i=0; i<monsters.size(); i++){
    if (monsters[i] > curr){
      counts += monsters[i] - curr;
      curr += 1;
    }
    else if(monsters[i] == curr){
      curr += 1;
    }
  }
  printf("%lld\n",counts);
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
