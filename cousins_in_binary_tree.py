
# https://leetcode.com/problems/cousins-in-binary-tree/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	# O(n) time, O(n) space
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		def depth_parent(root, target, depth, parent):
			if not root: return 
			if root.val == target: return depth, parent
			return depth_parent(root.left, target, depth + 1, root.val) or depth_parent(root.right, target, depth + 1, root.val)
		depth_x, parent_x = depth_parent(root, x, 0, None)
		depth_y, parent_y = depth_parent(root, y, 0, None)
		return depth_x == depth_y and parent_x != parent_y