# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        def encode(i: int):
            temp = None
            for val in str(i):
                node = ListNode(val)
                node.next = temp
                temp = node
            return node

        liste_1 = list()
        while l1 != None:
            liste_1.append(l1.val)
            l1 = l1.next

        liste_2 = list()
        while l2 != None:
            liste_2.append(l2.val)
            l2 = l2.next

        nb1 = 0
        for i in range(len(liste_1)):
            nb1 += liste_1[i] * (10**i)

        nb2 = 0
        for i in range(len(liste_2)):
            nb2 += liste_2[i] * (10**i)

        total = nb1 + nb2
        return encode(total)
