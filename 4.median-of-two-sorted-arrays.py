#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.kth(nums1, nums2, (len(nums1) + len(nums2)) // 2)
        else: 
            return (
                self.kth(nums1, nums2, (len(nums1) + len(nums2)) // 2) + 
                self.kth(nums1, nums2, (len(nums1) + len(nums2)) // 2 - 1)
                ) / 2  
        
    def kth(self, A, B, k):
        # Base case here TODO
        print(A)
        print(B)
        print()
        if not A:
            return B[k]
        elif not B:
            return A[k]

        m_a = len(A) // 2
        m_b = len(B) // 2
        n_a = A[m_a]
        n_b = B[m_b]

        # if k > m_a + m_b, oviousbly wwe need to delete some first half
        if k > m_a + m_b:
            # if m_a < m_b, we know that all element in the first half of A
            # EVEN the MEDIAN itself should not be the k-1_th element 
            if n_a < n_b:
                return self.kth(A[m_a +1:], B, k - m_a - 1)
            else:
                return self.kth(A, B[m_b +1:], k - m_b - 1)
        else: 
            if n_a > n_b:
                return self.kth(A[:m_a], B, k)
            else:
                return self.kth(A, B[:m_b], k)

# @lc code=end

