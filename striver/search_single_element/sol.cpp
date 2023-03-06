// the solution doesent work for a broader range of test cases !! useless 
#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> v {1,1,2,3,3,4,4,8,8};
  int enums = 0;
  for(int i=0; i<v.size(); i++){
    enums = enums ^ v[i];
  }
  printf("%d",enums);
}
