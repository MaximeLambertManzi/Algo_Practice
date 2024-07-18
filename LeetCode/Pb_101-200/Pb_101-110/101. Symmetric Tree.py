# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
