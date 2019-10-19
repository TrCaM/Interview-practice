#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # max for hour = 11 | max for minutes 59
        def backtrack(num, hours, mins, nxt):
            if hours > 11 or mins > 59:
                return
            if num == 0:
                output.append(transform(hours, mins))
                return

            for i in range(nxt, 10):
                if i < 4:
                    backtrack(num - 1, hours + 2**i, mins, i + 1)
                else:
                    k = i - 4
                    backtrack(num - 1, hours, mins + (1 << k), i + 1)

        def transform(hour, minute):
            minuteStr = "0" + str(minute) if minute < 10 else minute
            return f"{hour}:{minuteStr}"

        output = []
        backtrack(num, 0, 0, 0)
        
        return output
            
        
        
# @lc code=end

