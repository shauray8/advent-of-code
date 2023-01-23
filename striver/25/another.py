# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverselist(node1):
    prev,curr = None, node1
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = curr.next

    curr = prev
    while True:
        print(curr.val)
        if curr.next is None:
            break

        curr = curr.next
        
node1 = ListNode("3")
node2 = ListNode("4")
node3 = ListNode("5")
node4 = ListNode("6")

node1.next = node2
node2.next = node3
node3.next = node4

curr = node1
while True:
    print(curr.val)
    if curr.next is None:
        break

    curr = curr.next

print("-------------")
reverselist(node1)

