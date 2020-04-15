#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# [1, 0, 3, 5]
# [2, 1, 4, 6, 7]

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            other = target - num
            if other in map:
                return [i, map[other]]
            map[num] = i
# @lc code=end
