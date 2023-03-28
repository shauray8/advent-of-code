#include <bits/stdc++.h>

using namespace std;

int main(){
  string s = "this is a good program";
  string some;
  stack<string> st;
  for(int i=0; i<s.size(); i++){
    if (s[i] != " "){
      st.push(some);
      some = ""
    }
    else{
      some += s[i];
    }
  }
}
