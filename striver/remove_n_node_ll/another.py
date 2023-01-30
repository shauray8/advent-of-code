# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode()
        start.next = head
        l1 = l2 = start
        count = 0
        while l1.next:
            l1 = l1.next
            count += 1
        print(count)
        
        while count-n:
            l2 = l2.next
            count-=1
        l2.next = l2.next.next
        return start.next
