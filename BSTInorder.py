# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def bsf(node):
            if node:
                bsf(node.left)
                result.append(node.val)
                bsf(node.right)

        result = []
        bsf(root)
        return result

