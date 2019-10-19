#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permutate(S):
            if len(S) == 0:
                return [""]
            nextPermuates = permutate(S[1:])
            cur = None
            if S[0].isalpha():
                cur = [S[0].lower(), S[0].upper()]
            else:
                cur = [S[0]]
            result = []
            for first in cur:
                for rest in nextPermuates:
                    result.append(first + rest)
            return result
                
        return permutate(S)
        
# @lc code=end

