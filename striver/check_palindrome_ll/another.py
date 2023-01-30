# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = lag = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while lag != slow:
                    lag = lag.next
                    slow = slow.next
                return lag
        return None