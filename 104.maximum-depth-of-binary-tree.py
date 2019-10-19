#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthIter(root)

    def maxDepth_recursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepthIter(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        s = []
        m= 0
        s.append((1, root))
        while len(s):
            depth, cur = s.pop()
            m = max(depth, m)
            if cur.left:
                s.append((depth + 1, cur.left))
            if cur.right:
                s.append((depth + 1, cur.right))
        
        return m

        
# @lc code=end

