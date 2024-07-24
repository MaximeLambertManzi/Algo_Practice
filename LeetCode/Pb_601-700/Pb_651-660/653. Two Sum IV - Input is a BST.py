""" Given the root of a binary search tree and an integer k,
return true if there exist two elements in the BST such that their sum
is equal to k, or false otherwise

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105 """


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
