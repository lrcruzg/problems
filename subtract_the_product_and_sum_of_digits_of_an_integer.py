
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
	# O(Log_10(n)) time, O(1) space
	def subtractProductAndSum(self, n: int) -> int:
		sum_counter  = 0
		prod_counter = 1
		while n:
			sum_counter += n % 10
			prod_counter *= n % 10
			n //= 10
		return prod_counter - sum_counter