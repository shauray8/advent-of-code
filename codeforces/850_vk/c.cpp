#include <bits/stdc++.h>
using namespace std;

#define ll long long

int counts = 0;
vector<int> kill_once(vector<int> monsters, int index){
  for(int i=0; i<monsters.size(); i++){
    if (monsters[i] > index){
      counts += monsters[i]-index;
      monsters[i] = index;
      return monsters;
    }
  }
}

void solve(){
  int x;
  scanf("%d",&x);
  vector<int> monsters;
  int xx = x;
  while(x--){
    int m;
    scanf("%d",&m);
    monsters.push_back(m);
  }
  int results = 1;
  sort(monsters.begin(), monsters.end());
  for(int i=1; i<xx; i++){
    results = count(monsters.begin(), monsters.end(), i);
    if (results <= 0){
      monsters = kill_once(monsters,i);
    }
  }
  printf("%d\n",counts);
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
