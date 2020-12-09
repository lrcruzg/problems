
# https://leetcode.com/problems/path-crossing/

class Solution:
	# O(n) time, O(n) space
	def isPathCrossing(self, path: str) -> bool:
		position = (0,0)
		visited = set()
		visited.add(position)
		move = {"N":(0,1), "S":(0,-1), "E":(1,0), "W":(-1,0)}

		for c in path:
			position = (position[0] + move[c][0], position[1] + move[c][1])
			if position in visited:
				return True
			else:
				visited.add(position)
		return False