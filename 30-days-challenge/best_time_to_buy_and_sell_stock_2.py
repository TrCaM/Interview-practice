class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
      return 0
    low = 0
    profit = 0
    for i in range(1, len(prices)):
      profit += max(prices[i] - prices[i-1], 0)
    return profit
