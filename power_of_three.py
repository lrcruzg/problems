
# https://leetcode.com/problems/power-of-three/

class Solution:
	# O(n) time, O(n) space (recursion stack)
	def isPowerOfThree(self, n: int) -> bool:
		if n == 0: return False
		if n == 1: return True
		if n % 3 == 0:
			return self.isPowerOfThree(n // 3)
		return False

	'''
	# O(n) time, O(1) space
	def isPowerOfThree(self, n):
		if n == 0: return False
		while(n % 3):
			n //= 3
		return n == 1
	'''