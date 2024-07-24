""" Given the root of a binary tree,
invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertDFS(self, root):
        if root is None:
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
