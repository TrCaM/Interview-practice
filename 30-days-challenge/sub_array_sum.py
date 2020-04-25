from collections import defaultdict

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    levels = defaultdict(int)
    cur = 0
    results = -1 if k == 0 else 0
    levels[0] = 1
    for num in nums:
      cur += num 
      levels[cur] += 1
      total += levels[cur - k]
    return results 


        
