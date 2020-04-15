#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs2(self, n: int, mem = [0, 1, 2]) -> int:
        if len(mem) < n + 1:
            mem.append(self.climbStairs(n-1, mem) + self.climbStairs(n-2, mem))
        
        return mem[n]
    
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prevs = (1, 2)

        for _ in range(3, n + 1):
            prevs = prevs[1], prevs[1] + prevs[0]
        
        return prevs[1]

# @lc code=end

