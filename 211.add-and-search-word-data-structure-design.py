#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
from collections import defaultdict

class TrieNode:
    def __init__(self, end = False):
        self.end = end
        self.children = defaultdict(TrieNode)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(True)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            cur = cur.children[c] 
        cur.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, cur):
            if not word:
                return cur.end
            
            next = word[1:]
            if word[0] != '.':
                return False if word[0] not in cur.children else helper(next, cur.children[word[0]])


            return any([helper(next, cur.children[child]) for child in cur.children])
        return helper(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

