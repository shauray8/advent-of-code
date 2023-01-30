#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix = {1,0,-1,0,-2,2};
  set<vector<int>> hash;
  int target = 0;

  for(int i=0; i<matrix.size(); i++){
    for(int j=i+1; j<matrix.size(); j++){
      for(int k=j+1; k<matrix.size(); k++){
        int x = target - matrix[i] - matrix[j] - matrix[k];
        
        if(binarysearch(matrix.begin()+k+1, matrix.end(),x)){
          vector<int> v = {matrix[i],matrix[j],matrix[k],x};
          sort(v.begin(),v.end());
          hash.insert(v);
        }
      }
    }
  }
  vector<vector<int>> ans(hash.begin(),hash.end());
  return ans;

}
