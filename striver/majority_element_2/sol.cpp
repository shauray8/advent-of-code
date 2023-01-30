#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> nums = {2,1,2,2,2,1,1,3,2};
  int count = 0, candidate = 0;
  for(int num : nums){
    if (count == 0){
      candidate = num;
      count += 1;
    }
    if(count > 0 && candidate != num){
      count -= 1;
    }
  }
  printf("%d",candidate);
}
