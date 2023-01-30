# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None: return head 
        length = head
        count = 0
        while length:
            length = length.next
            count+=1
        k = k % count
        for i in range(k):
            temp = head
            while(temp.next.next):
                temp = temp.next
            next_guy = temp.next
            temp.next = None
            next_guy.next = head
            head = next_guy
        return head
            
            
