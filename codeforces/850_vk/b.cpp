#include <bits/stdc++.h>
using namespace std;

const long long INF = 9223372036854775807;

void solve(){
  int x;
  scanf("%d",&x);
  int a_white = 1, a_black = 0,b_white = 0,b_black = 0;
  int ll = 1;
  int black_white = 1;
  int suma = 2;
  x-=1;
  while(x>0){
    if(ll==0){
      for(int j=0; j<2; j++){
        if(x<=suma) suma=x;
        for(int k=0; k<suma; k++){
          if(black_white == 1){
            a_black++;
            x--;
            black_white = -black_white;
          }
          else{
            a_white++;
            x--;
            black_white = -black_white;
          }
        }
        suma++;
      }
      ll = 1;
    }
    else{
      for(int j=0; j<2; j++){
        if(x<=suma) suma=x;
        for(int k=0; k<suma; k++){
          if(black_white == 1){
            b_black++;
            x--;
            black_white = -black_white;
          }
          else{
            b_white++;
            x--;
            black_white = -black_white;
          }
        }
        suma++;
      }
      ll = 0;
    }
  }
  printf("%d %d %d %d \n",a_white,a_black,b_white,b_black);
}

int main(){
  ios_base::sync_with_stdio(0);
  //cin.tie(0);

  int n;
  scanf("%d",&n);
  while(n--){
    solve();
  }
}
