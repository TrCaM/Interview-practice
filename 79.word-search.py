#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(word, row, col, visited = set()):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            if (row, col) in visited or word[0] != board[row][col]:
                return False
            
            if len(word) == 1:
                return True

            visited.add((row, col))
            result =  dfs(word[1:], row + 1, col, visited) \
                or dfs(word[1:], row - 1, col, visited) \
                or dfs(word[1:], row, col + 1, visited) \
                or dfs(word[1:], row, col - 1, visited)
            
            visited.remove((row, col))
            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, i, j):
                    return True
        
        return False

