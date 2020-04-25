class Solution:
  def countElements(self, arr: List[int]) -> int:
    unique_nums = set(arr)
    count = 0
    for num in arr:
      count += 1 if num + 1 in unique_nums else 0

    return count


