
# https://leetcode.com/problems/clone-graph/

class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		def clone(node):
			if not node: return node
			tmp = Node(node.val)
			visited[node.val] = tmp
			for i in node.neighbors:
				if i.val not in visited:
					tmp.neighbors.append(clone(i))
				else:
					tmp.neighbors.append(visited[i.val])
			return tmp
		visited = {}
		return clone(node)
