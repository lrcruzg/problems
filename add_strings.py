
# https://leetcode.com/problems/add-strings/

class Solution:
	# O(n + m) time, O(n + m) space
	# where n = len(num1) and m = len(num2)
	def addStrings(self, num1: str, num2: str) -> str:
		return self.num_to_string(self.string_to_num(num1) + self.string_to_num(num2))
	
	def string_to_num(self, num):
		n = 0
		for i in range(len(num)):
			n = n * 10 + int(num[i])
		return n

	def num_to_string(self, n):
		if n == 0: return "0"
		s = ""
		while n:
			s += str(n % 10)
			n //= 10
		return s[::-1]