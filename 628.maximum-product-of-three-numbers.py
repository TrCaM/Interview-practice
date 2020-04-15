#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maximum = nums[0] * nums[1] * nums[2]
        nums.sort() 
        
        return max(nums[-1]* nums[-2]* nums[-3], nums[-1] * nums[0] * nums[1])

# @lc code=end

