/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
       unordered_set<ListNode*> set; 
       int count = 0;
       while(head!=NULL) {
           if(set.find(head) != set.end()) return head;
           set.insert(head);
           head = head->next;
           count++;
       }
       return NULL;
    }
};
