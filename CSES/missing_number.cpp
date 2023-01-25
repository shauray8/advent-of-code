#include <bits/stdc++.h>

using namespace std;

int main(){
  int n;
  scanf("%d",&n);
  vector<int> list;
  vector<int> another_list(n,0);
  for(int i=0; i<n-1;i++){
    int more;
    scanf("%d",&more);
    list.push_back(more);
  }
  for(int i=0; i<n; i++){
    another_list[list[i]] = 1;
  }
  for(int i =0; i<n; i++){
    if (another_list[i] == 0){
      printf("%d",i);
    }
  }



}
