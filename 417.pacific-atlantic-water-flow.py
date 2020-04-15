#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(r, c, visited):
            q = deque()
            q.append((r,c))

            while len(q):
                i, j = q.popleft()
                visited[i][j] = 1
                for dir in self.directions:
                    row, col =  i + dir[0], j + dir[1]
                    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]) or \
                        visited[row][col] or matrix[row][col] < matrix[i][j]:
                        continue
                    q.append((row, col))
            
        def dfs(r, c, prev, visited):
            if r < 0 or c < 0 or r == len(matrix) or c == len(matrix[0]) or visited[r][c]:
                return
            
            if prev <= matrix[r][c]:
                visited[r][c] = 1
                dfs(r+1, c, matrix[r][c], visited)
                dfs(r-1, c, matrix[r][c], visited)
                dfs(r, c+1, matrix[r][c], visited)
                dfs(r, c-1, matrix[r][c], visited)

        if not matrix:
            return []
        visited1 = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        visited2 = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        output = []
        for r in range(len(matrix)):
            # dfs(r, 0, matrix[r][0], visited1)
            bfs(r, 0, visited1)
        for c in range(len(matrix[0])):
            # dfs(0, c, matrix[0][c], visited1)
            bfs(0, c, visited1)

        for r in range(len(matrix)):
            # dfs(r, len(matrix[0]) -1, matrix[r][-1], visited2)
            bfs(r, len(matrix[0]) -1, visited2)
        for c in range(len(matrix[0])):
            # dfs(len(matrix) -1, c, matrix[-1][c], visited2)
            bfs(len(matrix) -1, c, visited2)

        print(visited1)
        print(visited2)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if visited1[r][c] > 0 and visited2[r][c] > 0:
                    output.append((r,c))
        
        return output
# @lc code=end

