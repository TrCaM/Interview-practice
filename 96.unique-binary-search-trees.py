#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n
        mem = [0] * (n + 1)
        mem[0], mem[1] = 1, 1

        for v in range(2, n+1):
            for r in range(1, v+1):
                mem[v] += mem[r - 1] * mem[v - r]
        
        return mem[n]
        
# @lc code=end

