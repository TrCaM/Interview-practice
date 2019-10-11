#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0  # 0
        p2 = 0  # 0
        cur = 0
        temp = nums1[:m]

        while p1 < m and p2 < n: 
            if temp[p1] < nums2[p2]: # 1 
                nums1[cur] = temp[p1]
                p1 += 1
            else:
                nums1[cur] = nums2[p2]
                p2 += 1
            cur += 1
        
        while p1 < m:
            nums1[cur] = temp[p1]
            p1 += 1
            cur += 1

        while p2 < n:
            nums1[cur] = nums2[p2]
            p2 += 1
            cur += 1
        
# @lc code=end

