# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    cur = dummy_node = ListNode()
    
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        else:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
    cur.next = list1 or list2
    return dummy_node.next 



        