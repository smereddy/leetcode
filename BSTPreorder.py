# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
# 1
# \
# 2
# /
# 3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ls = []

    def preorderTraversal(self, root):
        def dfs(node):
            if not node:
                return
            pre_order.append(node.val)
            dfs(node.left)
            dfs(node.right)

        pre_order = []
        dfs(root)
        return pre_order


