#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
import math

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        def calculateCell(row, col, M):
            s = 0
            counter = 0
            for i in range(max(row-1, 0), min(row+2, len(M))):
                for j in range(max(col-1, 0), min(col+2, len(M[0]))):
                    s += M[i][j]
                    counter += 1
            return math.floor(s / counter)             

        result = [row.copy() for row in M]

        for i in range(len(M)):
            for j in range(len(M[0])):
                result[i][j] = calculateCell(i, j, M)
        
        return result

# @lc code=end

