#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    class TrieNode:
        def __init__(self, end = False):
            self.end = end
            self.children = [None] * 26


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode(True)


    def index(self, char):
        return ord(char) - ord('a')


    def goDeep(self, word: str) -> TrieNode:
        cur = self.root
        for i in range(len(word)):
            nxt = cur.children[self.index(word[i])]
            if not nxt:
                return cur, word[i:]
            cur = nxt
        return cur, ""
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node, re = self.goDeep(word)
        if re:
            for i in range(len(re)):
                index = self.index(re[i])
                node.children[index] = self.TrieNode()
                node = node.children[index]
        node.end = True

        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node, re = self.goDeep(word)
        return not re and node.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return not self.goDeep(prefix)[1]
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

