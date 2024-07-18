# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, is_left):
        if root == None:
            return

        if root.left == None and root.right == None:
            if is_left:
                self.sum += root.val

        self.dfs(root.left, True)
        self.dfs(root.right, False)

    def sumOfLeftLeaves(self, root) -> int:

        self.sum = 0
        self.dfs(root, False)

        return self.sum
