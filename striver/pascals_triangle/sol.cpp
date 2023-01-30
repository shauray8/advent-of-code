#include <bits/stdc++.h>

using namespace std;

int main(){
  int num = 5;
  vector<vector<int>> dummy(num);
  for(int i=0; i<num; i++){
    dummy[i].resize(i+1);
    dummy[i][0] = 1;
    dummy[i][i] = 1;
    for(int j = 1; j<i; j++){
      dummy[i][j] = dummy[i-1][j-1] + dummy[i-1][j];
    }
    
  }

  for(int i=0; i<num; i++){
    for(int j=0; j<dummy[i].size(); j++){
      printf("%d",dummy[i][j]);
    }
  }
}
