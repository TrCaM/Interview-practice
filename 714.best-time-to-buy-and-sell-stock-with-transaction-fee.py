#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # if len(prices) <= 1:
        #     return 0
        # n = len(prices) 
        # profits = [0] * (n+1)
        

        # for sell in range(2, n+1):
        #     profits[sell] = max(
        #         [profits[buy -1] + prices[sell-1] - prices[buy-1] - fee for buy in range(1, sell)] + [profits[sell - 1]])
        cash = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
            print(cash, hold)
        
        return cash


# @lc code=end

