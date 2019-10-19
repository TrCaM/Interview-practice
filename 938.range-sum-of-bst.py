#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def traverse(node):
            if not node:
                return 0    
            val = node.val
            sum = traverse(node.left) if val > L else 0
            sum += node.val if node.val >= L and node.val <= R else 0
            sum += traverse(node.right) if val < R else 0
            return sum

        return traverse(root)


        
# @lc code=end

