#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<int> array = {5,4,3,2,1};

  int count = 0; 
  for(int i=0; i<array.size(); i++){
    for(int j=i; j<array.size(); j++){
      if (array[i] > array[j]){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        count++;
      }
    }
  }
  printf("%d",count);
}
