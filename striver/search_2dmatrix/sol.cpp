#include <bits/stdc++.h>

using namespace std;

int search(vector<vector<int>> matrix, int n){
  for(int i=0; i<matrix.size(); i++){
    if(matrix[i][matrix.size()] >= n){
      int start = 0, end = matrix.size(), mid =matrix[i][(start + end) / 2];
      while(start != end){
        if (n == mid){
          return true;
        }
        else if (n < mid){
          end = (start + end) / 2;
        }
        else{
          start = (start + end) / 2 ;
        }
      }
      return false;
    }
  }
  return false;
}

int main(){
  vector<vector<int>> matrix = {{1,3,5,7}, {10,11,16,20}, {23,30,34,60}};
  int n = 3;
  bool geto = search(matrix, n);
  printf("%d",geto);
}
