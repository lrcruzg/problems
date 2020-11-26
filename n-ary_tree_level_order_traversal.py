
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from collections import deque
from typing import List

class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children

class Solution:
	# O(n) time, O(n) space
	def levelOrder(self, root: 'Node') -> List[List[int]]:
		if not root: return []
		ans = []
		q = deque([root])
		while q:
			n = len(q)
			curr_lev = []
			for _ in range(n):
				node = q.popleft()
				curr_lev.append(node.val)
				for c in node.children:
					q.append(c)
					ans.append(curr_lev)
		return ans