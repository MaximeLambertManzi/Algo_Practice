""" Given the root of a binary tree,
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively? """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):

        res = []

        queue = []
        queue.append(root)

        while queue:
            len_queue = len(queue)
            level = []
            for i in range(len_queue):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level.append(0)
            if level:
                res.append(level)

        return res

    def isSymmetric(self, root) -> bool:
        left = []
        right = []

        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        if len(left) != len(right):
            return False

        for i in range(len(left)):
            if len(left[i]) != len(right[i]):
                return False
            if left[i] != right[i][::-1]:
                return False

        return True
