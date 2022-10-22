from typing import Optional

# https://leetcode.com/problems/path-sum-iii/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time.
	# O(n) space.
	# where n = number of nodes in the tree.
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
		def dfs(node, targetSum, prev):
			if not node:
				return

			curr_sum = prev + node.val

			if curr_sum - targetSum in path_prefix_sum:
				self.num_paths += path_prefix_sum[curr_sum - targetSum]
			
			if curr_sum in path_prefix_sum:
				path_prefix_sum[curr_sum] += 1;
			else:
				path_prefix_sum[curr_sum] = 1

			dfs(node.left , targetSum, curr_sum)
			dfs(node.right, targetSum, curr_sum)

			if path_prefix_sum[curr_sum]:
				path_prefix_sum[curr_sum] -= 1;

		self.num_paths = 0
		path_prefix_sum = {0:1}
		dfs(root, targetSum, 0)
		return self.num_paths
