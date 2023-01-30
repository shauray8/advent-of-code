/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL or head->next == NULL) return head;
        ListNode* temp = head;
        int count = 1;
        while (temp->next!=NULL){
            temp = temp->next;
            count++;
        }
        temp->next = head;
        k = k%count;
        int out = count-k;
        while(out--){
            temp = temp->next;
        }
        head = temp->next;
        temp->next = NULL; 
        return head;
        
    }
};
