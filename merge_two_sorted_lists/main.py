# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    if list1.val > list2.val:
        list1, list2 = list2, list1 # I want list1 to have the smaller starting value

    new_head = list1
    list1 = list1.next
    cur = new_head
    while list1 != None or list2 != None:
        if list1 == None:
            cur.next = list2
            break
        if list2 == None:
            cur.next = list1
            break

        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        else:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

    return new_head



        