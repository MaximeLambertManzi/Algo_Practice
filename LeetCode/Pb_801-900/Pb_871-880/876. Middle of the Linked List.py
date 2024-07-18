# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        count = 0
        node = head
        mid = head

        while node:
            count += 1
            node = node.next

        for i in range(count // 2):
            mid = mid.next

        return mid
