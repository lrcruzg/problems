
# https://leetcode.com/problems/roman-to-integer/

class Solution:
	# O(n) time, O(1) space
	# where n = len(s)
	def romanToInt(self, s: str) -> int:
		val = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		can_substract = {"I":"XV", "X":"LC", "C":"DM"}
		ans, i = 0, 0
		while(i < len(s) - 1):
			if s[i] in "IXC": 		# may have to substract
				# look at the next char to see if 
				# I need to substract									
				if s[i + 1] in can_substract[s[i]]:	# I have to substract s[i] to s[i + 1]
					ans += val[s[i + 1]] - val[s[i]]
					i += 2
				else: # I don't have to substract
					ans += val[s[i]]
					i += 1
			else: # s[i] in "VLDM", don't have to substract
				ans += val[s[i]]
				i += 1

		# last char
		if i < len(s):
			ans += val[s[-1]]

		return ans