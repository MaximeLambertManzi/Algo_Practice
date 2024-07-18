# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self, root, pre_trav):
        if root:
            pre_trav.append(root.val)
            self.trav(root.left, pre_trav)
            self.trav(root.right, pre_trav)
        else:
            return 0

    def preorderTraversal(self, root):
        pre_trav = []

        self.trav(root, pre_trav)

        return pre_trav
