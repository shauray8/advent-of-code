#include <bits/stdc++.h>

using namespace std;

int pow(int mid, int m){
  int ans = 1;
  for(int i=0; i<m; i++){
    ans *= mid;
  } 
  return ans;
}

int cubes(int m, int n){
  int start = 0, end = n;
  while(start <= end){
    int mid = start + (-start + end) / 2;
    int ans = pow(mid,m);
    if(ans == n){
      printf("%d",mid);
      return 0;
    }
    if(ans > n){
      end = mid-1;
    }
    else{
      start = mid+1;
    }
  }
}

int main(){
  int m = 5, n = 243;
  cubes(m,n);
}
