#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
import functools

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def product(l):
            if not l:
                return 0
            return functools.reduce(lambda a,b: a*b, l, 1)

        start = 0
        end = 0
        negatives = 0
        firstNeg = start - 1
        lastNeg = start - 1

        out = nums[0]
        if len(nums) > 1:
            for end in range(len(nums) + 1):
                if end == len(nums) or nums[end] == 0:
                    if negatives % 2 == 0:
                        out = max(out, 0, product(nums[start:end]))
                    else:
                        out = max(out, 0, product(nums[start:lastNeg]), product(nums[firstNeg +1:end]))

                    start = end + 1
                    fisrtNeg = lastNeg = start - 1
                    negatives = 0
                elif nums[end] < 0:
                    firstNeg = firstNeg if negatives > 0 else end
                    lastNeg = end
                    negatives += 1
        
        return out

                
    
        
# @lc code=end

