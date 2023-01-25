#include <bits/stdc++.h>

using namespace std;

int main(){
  long long n;
  scanf("%llu",&n);
  printf("%llu ",n);
  while (n!=1){
    if(n % 2 == 0){
      n /= 2;
      printf("%llu ",n);
    }
    else{
      n = (n*3) + 1;
      printf("%llu ",n);
    }
  }
}
