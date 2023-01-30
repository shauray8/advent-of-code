# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_diff(self,headA,headB):
        len1,len2 = 0,0
        while headA:
            len1 += 1
            headA = headA.next
        while headB:
            len2 += 1
            headB = headB.next
        return len1 - len2

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        diff = self.get_diff(headA,headB)
        if diff < 0:
            while diff:
                headB = headB.next
                diff += 1
        else:
            while diff: 
                headA = headA.next
                diff -= 1
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
