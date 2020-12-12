
# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
	# O(n) time, O(n) space (stack)
	# n = len(s)
	def calculate(self, s: str) -> int:
		if not s: return 0
		numbers = "0123456789"
		stack = []
		current_op = "+"
		current_num = 0
		for i, c in enumerate(s):
			if c in numbers:
				current_num = current_num * 10 + int(c)
			if c in "+-*/" or i == len(s) - 1:
				if current_op == "-":
					current_num *= -1
				if current_op in "*/":
					prev_num = stack.pop()
					if current_op == "*":
						current_num *= prev_num 
					else: # current_op == "/"
						if prev_num // current_num < 0 and prev_num % current_num != 0:
							current_num = prev_num // current_num + 1
						else:
							current_num = prev_num // current_num
				stack.append(current_num)
				current_num = 0
				current_op = c
		return sum(stack)