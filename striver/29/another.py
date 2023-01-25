# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x,y = "",""
        another = ListNode(0)
        start = another
        while l1:
            x += str(l1.val)
            l1 = l1.next
        while l2:
            y += str(l2.val)
            l2 = l2.next
        z = int(x[::-1])+int(y[::-1])
        print(z)
        for i in str(z)[::-1]:
            some = ListNode(int(i))
            start.next = some
            start = start.next
        return another.next
