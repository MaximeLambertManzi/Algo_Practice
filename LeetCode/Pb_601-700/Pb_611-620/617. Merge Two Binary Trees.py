# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1, root2):

        if not root1 and not root2:
            return
        elif not root1:
            root0 = root2
        elif not root2:
            root0 = root1
        else:
            root0 = TreeNode(root1.val + root2.val)
            root0.left = self.mergeTrees(root1.left, root2.left)
            root0.right = self.mergeTrees(root1.right, root2.right)

        return root0
