class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    if not nums:
      return []

    out = [1] * len(nums)
    top = 1
    for i in range(0, len(nums)):
      out[i] =  top * num
      top = out[i]
    accumulate = 1
    for i in range(len(nums) - 1, 0, -1):
      out[i] = out[i-1] * accumulate
      accumulate *= nums[i]
    out[0] = accumulate

    return out
