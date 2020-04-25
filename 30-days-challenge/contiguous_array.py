class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    index_map = {0: 0}
    max_length = 0
    total = 0
    for i, num in enumerate(nums):
      total += 1 if num else -1
      if total not in index_map:
        index_map[total] = i+1
      max_length = max(max_length, i+1 - index_map[total])

    return max_length
