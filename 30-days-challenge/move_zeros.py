class Solution:
  def moveZeros(self, nums):
    sep = 0
    for i, n in enumerate(nums):
      if n != 0:
        nums[i], nums[sep] = nums[sep], nums[i]
        sep += 1
