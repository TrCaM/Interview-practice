#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return None
        
        med = len(nums) // 2
        root = TreeNode(nums[med])
        root.left = self.sortedArrayToBST(nums[0:med])
        root.right = self.sortedArrayToBST(nums[med+1:len(nums)])

        return root

        
# @lc code=end

