#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix ={1, 3, -5, 6, -2};
  int sigma = 0, pi = 0;
  unordered_map<int, int> hash_map;
  for(int i=0; i<matrix.size(); i++){
    sigma += matrix[i];
    if (sigma == 0){
      pi = max(pi, i+1);
    }
    else{
      if (hash_map.find(sigma) != hash_map.end()){
        pi = max(pi,i-hash_map[sigma]);
      }
      else{
        hash_map[sigma] = i;
      }
    }

  }
  printf("pi %d",pi);
}
