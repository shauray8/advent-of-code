#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> array = {3,1,2,5,4,6,7,5};
  int n = array.size();
  long long sum = (n*(n+1))/2;
  long long product = (n*(n+1)*(2*n+1))/6;
  long long s1, p1;

  for(int i=0; i<array.size(); i++){
    sum -= array[i];
    product -= array[i]*array[i];
  }

  int x,y;
  x = (sum + product/sum)/2;
  y = x - sum;

  printf("%d,%d",x,y);
  

}
