#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> matrix = {1,3,2,3,1};
  int sum = 0;
  for(int i=0; i<matrix.size(); i++){
    for(int j=i; j<matrix.size(); j++){
      if(i < j && matrix[i] > 2*matrix[j]){
        sum += 1;
      }
    }
  }
  printf("%d",sum);
}
