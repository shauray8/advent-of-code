#include <bits/stdc++.h>

using namespace std;

int factorial(int n){
  if (n == 1){
    return 1;
  }
  else{
    return n*factorial(n-1);
  }
}

int main(){
  int a = factorial(5);
  printf("%d",a);
}
