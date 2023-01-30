#include <bits/stdc++.h>

using namespace std;

int main(){
  int x;
  scanf("%d",&x);
  while(x--){
    int y,cc;
    vector<int> some;
    scanf("%d",&y);
    cc = y;
    while(y--){
      int z;
      scanf("%d",&z);
      some.push_back(z);
    }
    int global_count = 0;
    sort(some.begin(),some.end());
    int count = 0;
    for(int i=0; i<sizeof(some); i++){
      int count=0;
      for(int j=i; j<sizeof(some); j++){
        if(some[i]+1 == some[j]){
          count++;
        }
        else{
          break;
        }
      }
      if(count > 0){
        global_count++;
      }
    }
    }
    if (count > 0){
      global_count++;
    }
    printf("%d",global_count);
  }
}
