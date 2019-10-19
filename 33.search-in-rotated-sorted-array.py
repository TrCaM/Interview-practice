#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        while l < h:
            m = l + (h- l) // 2
            
            if nums[m] == target:
                return m
            
            if nums[m] > nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    h = m
            else:
                if target < nums[m] or target >= nums[l]:
                    h = m
                else:
                    l = m + 1
        return -1 
        # def search(nums, target, start, end):
        #     if start >= end: 
        #         return -1

        #     mid = start + (end - start) // 2
            
        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[mid] > nums[start]:
        #         if target > nums[mid] or target < nums[start]:
        #             return search(nums, target, mid + 1, end)
        #         else:
        #             return search(nums, target, start, mid)
        #     else:
        #         if target < nums[mid] or target >= nums[start]:
        #             return search(nums, target, start, mid)
        #         else:
        #             return search(nums, target, mid + 1, end)

        
        # return search(nums, target, 0, len(nums))
        
# @lc code=end

