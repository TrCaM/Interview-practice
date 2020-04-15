#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = [[0] * (n+1) for _ in range(m+1)]

        # Transform strs
        counts = [ (s.count('0'), s.count('1')) for s in strs]

        for zeros, ones in counts:
            for i in range(m, zeros -1, -1):
                for j in range(n, ones- 1, -1):
                    mem[i][j] = max(1 + mem[i - zeros][j- ones], mem[i][j])
        
        return mem[m][n]
        
# @lc code=end

