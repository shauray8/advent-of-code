#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> arr1 = {1,4,7,8,10};
  vector<int> arr2 = {2,3,9};

  for(int i=0; i<arr1.size(); i++){
    if (arr1[i] > arr2[0]){
      swap(arr2[0],arr1[i]);
      sort(arr2.begin(),arr2.end());
    }
  }

  for(int i=0; i<arr1.size(); i++){
    printf("%d",arr1[i]);
  }

}
