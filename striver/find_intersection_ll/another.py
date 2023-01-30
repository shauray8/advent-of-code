# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()
        other = headA
        while other:
            hash_set.add(other)
            other = other.next
        while headB:
            if headB in hash_set:
                return headB
            headB = headB.next
        return None
