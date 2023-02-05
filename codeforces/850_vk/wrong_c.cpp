#include <bits/stdc++.h>
using namespace std;

#define ll long long

int counts = 0;
vector<int> kill_once(vector<int> monsters){
  sort(monsters.begin(),monsters.end());
  for(int i=0; i<monsters.size(); i++){
    if (monsters[i] > 0){
      monsters[i]--;
      counts++;
      return monsters;
    }
  }
}

vector<int> kill_all(vector<int> monsters){
  for(int i=0; i<monsters.size(); i++){
    if (monsters[i] > 0){
      monsters[i]--;
    }
  }
  return monsters;
}

void solve(){
  int x;
  scanf("%d",&x);
  vector<int> monsters;
  while(x--){
    int m;
    scanf("%d",&m);
    monsters.push_back(m);
  }
  int results = accumulate(monsters.begin(), monsters.end(), 0);
  while(results){
    if (count(monsters.begin(), monsters.end(), 1) >= 1){
      monsters = kill_all(monsters);
      results = accumulate(monsters.begin(), monsters.end(), 0);
    }
    else{
      monsters = kill_once(monsters);
      results = accumulate(monsters.begin(), monsters.end(), 0);
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
