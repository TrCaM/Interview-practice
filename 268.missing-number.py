#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums) + 1):
            out ^= i
        
        for n in nums:
            out ^= n
        return out
        
# @lc code=end

