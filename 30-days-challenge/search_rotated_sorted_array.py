class Solution:
  def search(self, nums: List[int], target: int, left=0, right=-1) -> int:
    if right == -1:
      right = len(nums) - 1

    if right < left:
      return -1

    mid = left + (right - left + 1) // 2

    if nums[mid] == target:
      return mid
    if nums[left] == target:
      return left
    if nums[right] == target:
      return right

    if (nums[left] < nums[mid] and nums[mid] < target) or \
       (nums[mid] < target and target < nums[right]) or \
       (nums[mid] > nums[left] and target < nums[left]):
      return self.search(nums, target, mid+1, right-1)
    else:
      return self.search(nums, target, left+1, mid-1)

