#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix = {3, 8, 5, 7, 6};
  if(matrix.size() == 0){
    return 0;
  }
  int local_count = 1, global_count = 1, prev = matrix[0];
  for(int i=1; i<matrix.size(); i++){
    if (matrix[i] == prev){
      local_count += 1;
    }
    else if (matrix[i] != prev){
      local_count = 1;
    }
    global_count = max(local_count, global_count);
    prev = matrix[i];
  }
    
}
