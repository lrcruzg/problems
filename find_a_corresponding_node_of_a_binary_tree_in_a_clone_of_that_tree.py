
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
		q = deque([original])
		q_clone = deque([cloned])
		while q:
			tmp = q.popleft()
			tmp_clone = q_clone.popleft()
			if tmp == target:
				return tmp_clone
			if tmp.left:
				q.append(tmp.left)
				q_clone.append(tmp_clone.left)
			if tmp.right:
				q.append(tmp.right)
				q_clone.append(tmp_clone.right)
