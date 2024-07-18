# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        res = dummy = ListNode()

        while head:

            while head.next and head.val == head.next.val:
                head = head.next

            dummy.next = head
            dummy = dummy.next
            head = head.next

        return res.next
