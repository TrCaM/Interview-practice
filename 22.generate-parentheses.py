#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def genHelper(open, close, prev):
            if open == 0:
                output.append(prev + ")" * close)
                return
            
            # choose the next be open
            genHelper(open - 1, close, prev + "(")
            if open < close:
                genHelper(open, close-1, prev + ")")
            
        genHelper(n, n, "")
        return output


        
# @lc code=end

