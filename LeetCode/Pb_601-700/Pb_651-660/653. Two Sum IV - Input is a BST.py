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
            values.append(root.val)
            self.dfs(root.left, values)
            self.dfs(root.right, values)

    def findTarget(self, root, k: int) -> bool:
        values = []
        self.dfs(root, values)
        len_val = len(values)
        if len_val == 1:
            return False
        else:
            for i in range(len_val):
                target = k - values[i]
                for j in range(i + 1, len_val):
                    if values[j] == target:
                        return True
            target = 0

        return False
