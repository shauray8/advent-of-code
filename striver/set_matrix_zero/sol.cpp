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

int third(vector< vector <int>> & matrix){
  int col0 = 1;
  for(int i=0; i<matrix.size();i++){
    if(matrix[i][0] == 0){col0 = 0;}
    for(int j=1;j<matrix[0].size();j++){
      if(matrix[i][j] == 0){
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

 for(int i=matrix.size()-1; i>=0; --i){
    for(int j=matrix[0].size()-1; j>=0;--j){
      if(matrix[i][0] == 0 || matrix[0][j] == 0){
        matrix[i][j] = 0;
      }
    }
    if(col0 == 0){
      matrix[i][0] = 0;
    }
  }

}

int main(){
  vector< vector <int>> arr;
  arr = {{1,2,3,4},{5,0,7,8},{0,10,11,12},{13,14,15,0}};
  third(arr);
  for(int i=0; i<arr.size(); i++){
    for(int j=0; j<arr[0].size(); j++){
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }

}
