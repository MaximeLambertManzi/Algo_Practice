# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self, root, post_trav):
        if root:
            self.trav(root.left, post_trav)
            post_trav.append(root.val)
            self.trav(root.right, post_trav)
        else:
            return 0

    def postorderTraversal(self, root):
        post_trav = []

        self.trav(root, post_trav)

        return post_trav
