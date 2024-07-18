# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        set_val = set()

        while head != None:
            if head in set_val:
                return True
            else:
                set_val.add(head)

            head = head.next

        return False
