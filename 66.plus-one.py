#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mem = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            mem, digits[i] = divmod(digits[i] + mem, 10)
        
        if mem:
            digits = [1] + digits
        return digits
        
# @lc code=end

