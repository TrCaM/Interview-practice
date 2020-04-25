class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0

    self.visited = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
    grid = [list(map(int, row)) for row in grid]

    def dfs(i, j):
      nonlocal grid
      if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or not grid[i][j] or self.visited[i][j]:
        return
      
      self.visited[i][j] = 1
      dfs(i+1, j)
      dfs(i-1, j)
      dfs(i, j+1)
      dfs(i, j-1)

    total = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] and not self.visited[i][j]:
          total += 1
          dfs(i, j)

    return total

