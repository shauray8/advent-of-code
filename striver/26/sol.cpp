#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
       ListNode* curr = head;
       int count = 0;
       while(curr){
           curr = curr->next;
           count++;
       }
       curr = head;
       for(int i=0; i<int(count/2);i++){
           curr = curr->next;
       }
       return curr;
       
    }
};

int main(){
  return 1
}
