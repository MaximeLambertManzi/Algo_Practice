# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node"):

        if not root:
            return

        res = list()

        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))

        return res
