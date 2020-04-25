class Solution:
  def canJump(self, nums: List[int]) -> bool:
    min_start = len(nums) - 1

    for i in range(len(nums)- 2, -1, -1):
      if i + nums[i] >= min_start:
        min_start = i

    return min_start == 0
