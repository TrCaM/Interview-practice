class Solution:
  def minPathSum_bottom_up(self, grid: List[List[int]]) -> int:
    dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
    dp[-1][-1] = grid[-1][-1]

    if not grid:
      return 0
  
    for i in range(len(grid) - 2, -1, -1):
      dp[i][-1] += dp[i+1][-1]
    for j in range(len(grid[0]) - 2, -1, -1):
      dp[-1][j] += dp[-1][j+1]

    for i in rannge(len(grid) - 2, -1, -1):
      for j in range(len(grid[0]) - 2, -1, -1):
        dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]

    return dp[0][0]

  def minPathSum(self, grid: List[List[int]]) -> int:
    def dfs(i, j):
      nonlocal grid
      nonlocal dp

      if i >= len(grid) or j >= len(grid[0]):
        return float('inf')
      
      if dp[i][j] == -1:
        best_path = min(dfs(i+1, j), dfs(i, j+1))
        dp[i][j] = best_path + grid[i][j]
      
      return dp[i][j]

    if not grid:
      return 0
    dp = [[-1] * len(grid[0]) for _ in range(len(grid))]
    dp[-1][-1] = grid[-1][-1]
    return dfs(0, 0)
  

