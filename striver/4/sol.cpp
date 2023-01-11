#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix = {-1};
  vector<int> var = {0, INT_MIN};
  for(int i=0; i<matrix.size(); i++){
    var[0] = max(matrix[i], matrix[i]+var[0]);
    if (var[0] > var[1]){
      var[1] = var[0];
    }
  }
  printf("%d",var[1]);
}
