""" Given the head of a linked list,
remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass? """


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
