#include <bits/stdc++.h>

using namespace std;

vector<int> c_count;
int m = 3, n = 7;
vector<vector<int>> matrix(m, vector<int> (n, 0));  
vector<vector<int>> dummy(m+1, vector<int> (n+1, -1));

// recursive nature of the algo

int move(vector<int> path){
  int i = path[0], j = path[1];
  if(path[0] > m-1 || path[1] > n-1){
    return 0;
  }
  if(path[0] == m-1 && path[1] == n-1){
    c_count.push_back(1);
    return 1;
  }
  if(dummy[i][j] != -1){
    c_count.push_back(1);
    return dummy[i][j];
  }
  dummy[i][j] = move({i+1,j}) + move({i,j+1});
}

int main(){
  move({0,0});
  printf("%d",c_count.size());
}



//class Solution {
//public:
//    int uniquePaths(int m, int n) {
//        unsigned int t[m+1][n+1];
//        for (int i=0;i<m+1;i++){
//            for (int j=0;j<n+1;j++){
//                if (i==0 || j==0){
//                    t[i][j]=1;
//                }
//            }
//        }
//        for (int i=1;i<m+1;i++){
//            for (int j=1;j<n+1;j++){
//                t[i][j]=t[i-1][j]+t[i][j-1];            
//            }
//        }
//        return t[m-1][n-1];
//    }
//};
