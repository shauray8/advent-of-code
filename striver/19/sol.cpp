#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix = {2,7,11,15};
  int target = 9;
  for(int i=0; i<matrix.size(); i++){
    for(int j=i; j<matrix.size(); j++){
      if (matrix[i] + matrix[j] == target){
        return {matrix[i], matrix[j]};
      }
    }
  }

}
