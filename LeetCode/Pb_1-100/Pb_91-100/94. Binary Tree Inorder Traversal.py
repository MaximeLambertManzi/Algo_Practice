# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self, root, in_trav):
        if root:
            self.trav(root.left, in_trav)
            in_trav.append(root.val)
            self.trav(root.right, in_trav)
        else:
            return 0

    def inorderTraversal(self, root):
        in_trav = []

        self.trav(root, in_trav)

        return in_trav
