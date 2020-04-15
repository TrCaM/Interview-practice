#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def helper(r, d):
            if r == 0 or d == 0:
                return 1
            if (r, d) not in mem:
                mem[(r,d)] = helper(r - 1, d) + helper(r, d - 1)

            return mem[(r,d)]
        
        return helper(m-1, n-1)
        
# @lc code=end

