#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushToMostLeft(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.stack.pop()
        if n.right:
            self.pushToMostLeft(n.right)
        return n.val;
        

    def pushToMostLeft(self, node): 
        n = node
        while n:
            self.stack.append(n)
            n = n.left


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

