# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertDFS(self, root):
        if root == None:
            return 0
        else:
            if root.left and root.right:
                root.left, root.right = root.right, root.left
                self.invertDFS(root.left)
                self.invertDFS(root.right)
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
                self.invertDFS(root.right)
            elif root.right and not root.left:
                root.left = root.right
                root.right = None
                self.invertDFS(root.left)

    def invertTree(self, root):
        self.invertDFS(root)
        return root
