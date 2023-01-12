#include <bits/stdc++.h>

using namespace std;

int main(){
  vector<vector<int>> intervals = {{1, 3}, {2, 4}, {2, 6}, {8, 9}, {8, 10}, {9, 11}, {15, 18}, {16, 17}};
  vector<vector<int>> another = {intervals[0]};

  sort(intervals.begin(),intervals.end());

  for(int i=0; i<intervals.size(); i++){
    if(intervals[i][0] <= another[another.size()][1]){
      another[another.size()][1] = max(another[another.size()][1], intervals[i][1]);
    }
    else{
      another.push_back(intervals[i]);
    }
  }

  for(int i=0; i<intervals.size(); i++){
    for(int j=0; j<intervals[0].size(); j++){
      printf("%d",intervals[i][j]);
    }
  }
}
