
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children

class Solution:
	# O(n) time, O(n) space
	def maxDepth(self, root: Node) -> int:
		if not root: return 0
		max_depth = 1
		if root.children:
			for node in root.children:
				tmp = 1 + self.maxDepth(node)
				if tmp > max_depth:
					max_depth = tmp
		return max_depth