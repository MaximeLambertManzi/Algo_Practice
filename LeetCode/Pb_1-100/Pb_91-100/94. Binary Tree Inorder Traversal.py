""" Given the root of a binary tree,
return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively? """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trav(self, root, in_trav):
        if root:
            self.trav(root.left, in_trav)
            in_trav.append(root.val)
            self.trav(root.right, in_trav)
        else:
            return 0

    def inorderTraversal(self, root):
        in_trav = []

        self.trav(root, in_trav)

        return in_trav
