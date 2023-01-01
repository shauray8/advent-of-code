#include <bits/stdc++.h>

using namespace std;

int first(vector < vector <int>> & matrix){
  for(int i=0; i<matrix.size(); i++){
    for(int j=0; j<matrix[0].size(); j++){
      if(matrix[i][j] == 0){
        for(int k=0;k<matrix.size();k++){
          if(matrix[k][j] != 0){
            matrix[k][j] = -1;
          }
        }
        for(int k=0;k<matrix[0].size();k++){
          if(matrix[i][k] != 0){
            matrix[i][k] = -1;
          }
        }
      }
    }
  }

  for(int i=0; i<matrix.size(); i++){
    for(int j=0; j<matrix[0].size(); j++){
      if(matrix[i][j] == -1){
        matrix[i][j] = 0;
      }
    }
  }

}

int secoond(vector< vector <int>> & matrix){
  vector<int> row(matrix.size());
  vector<int> col(matrix[0].size());
  for(int i=0;i<matrix.size();i++){
    for(int j=0;j<matrix[0].size();j++){
      if(matrix[i][j] == 0){
        row[i] = -1;
        col[j] = -1;
      }
    }
  }
  for(int i=0;i<matrix.size();i++){
    for(int j=0;j<matrix[0].size();j++){
      if(row[i] == -1 || col[j] == -1){
        matrix[i][j] = 0;
      }
    }
  }
  
}

int main(){
  vector< vector <int>> arr;
  arr = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
  secoond(arr);
  for(int i=0; i<arr.size(); i++){
    for(int j=0; j<arr[0].size(); j++){
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }

}
