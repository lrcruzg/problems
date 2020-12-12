
# https://leetcode.com/problems/path-sum-ii/

from typing import List

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
		def dfs(node, current_path, current_sum):
			if not node: return
			if not node.left and not node.right and current_sum + node.val == sum:
				self.paths.append(current_path + [node.val])
			dfs(node.left,  current_path + [node.val], current_sum + node.val)
			dfs(node.right, current_path + [node.val], current_sum + node.val)
		self.paths = []
		dfs(root, [], 0)
		return self.paths