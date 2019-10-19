#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invertTree_recur(root):
            if  root:
                left = root.left
                right = root.right
                root.left = invertTree_recur(right)
                root.right = invertTree_recur(left)
            return root

        def invertTree_iter(root):
            s = [root]
            while len(s):
                cur = s.pop()
                if cur:
                    s.append(cur.left)
                    s.append(cur.right)
                    cur.right, cur.left = cur.left, cur.right
            return root

            

        return invertTree_iter(root)
        
# @lc code=end

