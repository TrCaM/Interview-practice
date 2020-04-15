#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []

        maps = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        listDigits = [int(char) for char in digits]
        listChars = [maps[digit] for digit in listDigits]
        

        output = []

        def letterCombiHelper(index, prev = ''):
            if index == len(listChars):
                output.append(prev)
                return 
            
            for c in listChars[index]:
                letterCombiHelper(index + 1, prev + c)
        
        letterCombiHelper(0)
        return output

# @lc code=end

