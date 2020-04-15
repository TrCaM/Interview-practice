#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        coins.sort()

        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin > i:
                    break
                if coin == i:
                    dp[i] = 1
                elif i > coin:
                    if dp[i] > -1 and dp[i-coin] > -1:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
                    elif dp[i - coin] > -1:
                        dp[i] = dp[i-coin] + 1
        
        return dp[amount]
                
        
# @lc code=end

 