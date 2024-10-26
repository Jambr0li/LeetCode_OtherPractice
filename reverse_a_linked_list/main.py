# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
head.next = second
second.next = third 
# print(head.val)
# print(second.next.val)
def reverseList(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

reverseList(head)



        