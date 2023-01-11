#include <bits/stdc++.h>

using namespace std;

int another(vector<vector<int>> matrix){
  vector<vector<int>> dummy(matrix.size(), vector<int> (matrix.size(),0));
  for(int i =0; i<matrix.size(); i++){
    for(int j=0; j<matrix[0].size(); j++){
      dummy[j][matrix.size()-i-1] = matrix[i][j];
    }
  }
}

int main(){
  vector<vector<int>> matrix = {{1,2,3},{4,5,6},{7,8,9}};

  for(int i =0; i<matrix.size(); i++){
    for(int j=0; j<i; j++){
      swap(matrix[i][j],matrix[j][i]);
    }
  }

  for(int i=0; i<matrix.size(); i++){
    reverse(matrix[i].begin(),matrix[i].end());
  }

  for(int i =0; i<matrix.size(); i++){
    for(int j=0; j<matrix[0].size(); j++){
      printf("%d",matrix[i][j]);
    }
  }
}
