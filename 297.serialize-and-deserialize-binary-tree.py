#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.
		
		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return ""

		out = []
		q = collections.deque()
		q.append(root)
		last = 0
		while len(q) > 0:
			cur = q.popleft()
			if cur:
				out.append(str(cur.val))
				last = len(out)
				q.append(cur.left)
				q.append(cur.right)
			else:
				out.append("n")

		return "|".join(out[:last])
		

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		
		:type data: str
		:rtype: TreeNode
		"""
		if not len(data):
			return None
		vals = data.split("|")
		root = TreeNode(int(vals[0]))
		queue = collections.deque() 
		queue.append(root)
		nxt = 1		

		while len(queue) > 0:
			cur = queue.popleft()

			if nxt < len(vals) :
				vl = vals[nxt]
				if vl != 'n':
					cur.left = TreeNode(int(vl))
					queue.append(cur.left)
				nxt += 1
			if nxt < len(vals) :
				vr = vals[nxt]
				if vr != 'n':
					cur.right = TreeNode(int(vr))
					queue.append(cur.right)
				nxt += 1
		
		return root
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

