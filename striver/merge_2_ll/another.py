## linked list


if list1 == None : return list2
if list2 == None : return list1
if list1.val > list2.val:
    list1,list2 = list2,list1
res = list1
while list1 and list2:
    temp = ListNode(None)
    while list1 != None and list1.val <= list2.val:
        temp = list1
        list1 = list1.next
    temp.next = list2
    list1,list2 = list2,list1
return res
