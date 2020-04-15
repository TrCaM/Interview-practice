#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def permuteHelper(nums, path):
            if not nums:
                output.append(path)
            
            for i in range(len(nums)):
                permuteHelper(nums[:i] + nums[i+1:], path + [nums[i]])

        permuteHelper(nums, [])
        return output

        
# @lc code=end

