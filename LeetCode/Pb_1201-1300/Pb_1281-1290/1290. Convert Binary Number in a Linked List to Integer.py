# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:

        bin_number = []
        dec_number = 0

        while head:
            bin_number.append(head.val)
            head = head.next

        len_bin = len(bin_number)

        for i in range(len_bin):
            dec_number += bin_number[i] * (2 ** (len_bin - (i + 1)))

        return dec_number
