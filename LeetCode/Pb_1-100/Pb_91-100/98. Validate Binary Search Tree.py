# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, values):
        if not root:
            return 0
        else:
            self.dfs(root.left, values)
            values.append(root.val)
            self.dfs(root.right, values)

    def isValidBST(self, root) -> bool:
        values = []
        self.dfs(root, values)
        # inorder DFS on BST is a sorted list
        is_valid = True
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                is_valid = False
                break

        return is_valid
