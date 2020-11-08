
# https://leetcode.com/problems/maximum-69-number/

class Solution:
	# O(log(n)) time, O(log(n)) space
	def maximum69Number (self, num: int) -> int:
		digits = []
		ans = 0
		change = True

		while num:
			digits.append(num % 10)
			num //= 10

		for i in range(len(digits) - 1, -1, -1):
			if digits[i] == 6 and change:
				digits[i] = 9
				change = False
			ans = ans * 10 + digits[i] 

		return ans

test = 9669
s = Solution()
print(s.maximum69Number(test))


s