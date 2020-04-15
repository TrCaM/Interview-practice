#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates = sorted(candidates)

        def helper(candidates, target, prev = []):
            if (target == 0):
                output.append(prev)
                return
            
            for i, candidate in enumerate(candidates):
                for recur in range(1, target // candidate + 1):
                    helper(candidates[i+1:], target - candidate * recur, prev + [candidate] * recur)
            
        helper(candidates, target)
        return output


            

        
# @lc code=end

