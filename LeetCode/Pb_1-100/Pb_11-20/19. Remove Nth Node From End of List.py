# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        count = 0
        nth_node = 0
        node = head

        while node:
            count += 1
            node = node.next

        nth_node = count - n

        dummy = head
        if count == n:
            return head.next
        elif count == 1:
            return None
        else:
            for i in range(nth_node - 1):
                dummy = dummy.next

            dummy.next = dummy.next.next
            return head
