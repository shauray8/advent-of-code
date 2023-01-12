#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> freq;
  vector<int> nums = {1,2,3,4,1};
  for(int i=0; i<nums.size(); i++){
    freq[nums[i]] += 1;
    if (freq[nums[i]] > 1){
      return nums[i];
    }
  }
}
