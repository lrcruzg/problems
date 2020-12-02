
# https://leetcode.com/problems/valid-parentheses/

class Solution:
	# O(n) time, O(n) space
	def isValid(self, s: str) -> bool:
		stack = []
		close = {"{":"}", "[":"]", "(":")"}
		for c in s:
			if c in "([{":
				stack.append(c)
			else:
				if len(stack) == 0 or close[stack[-1]] != c:
					return False
				else:
					stack.pop()
		return len(stack) == 0