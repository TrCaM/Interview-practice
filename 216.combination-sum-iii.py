#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9 or n > 45:
            return []

        out = []
        l = []
        def combi(k, n, start):
            # Base case
                
            cont = True
            # print(start)
            for i in range(start, 11 - k):
                l.append(i)
                if k == 1:
                    if n == i:
                        out.append(l.copy())
                        cont = False
                else:
                    combi(k - 1, n - i, i+1) 
                l.pop()
                if not cont:
                    break
        
        combi(k, n, 1)
        return out
        
# @lc code=end