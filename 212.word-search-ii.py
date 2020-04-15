#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from collections import defaultdict

class TrieNode:
    def __init__(self, end = False):
        self.children = defaultdict(TrieNode)
        self.end = False
        self.word = None


class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def buildTries(self, words):
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                cur = cur.children[char]
            cur.word = word
        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node):
            if node.word:
                output.add(node.word)
            visited[r][c] = 1

            for d in self.directions:
                nr, nc = r+d[0], c+d[1]
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or visited[nr][nc]:
                    continue
                nxt = board[nr][nc]
                if nxt in node.children:
                    dfs(nr, nc, node.children[nxt])
            visited[r][c] = 0

        output = set()
        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for _ in range(rows)]
        root = self.buildTries(words)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root.children[board[i][j]])


        return list(output)
        
# @lc code=end

