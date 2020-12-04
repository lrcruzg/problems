
# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
	# O(n) time, O(1) space
	def validPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1
		while l < r:
			if s[l] != s[r]:
				opt1, opt2 = True, True
				# s[l + 1:r] is palindrome
				l_aux, r_aux = l + 1, r
				while l_aux < r_aux:
					if s[l_aux] != s[r_aux]:
						opt1 = False
					l_aux += 1
					r_aux -= 1
				# s[l: r - 1] is palindrome
				l_aux, r_aux = l, r - 1
				while l_aux < r_aux:
					if s[l_aux] != s[r_aux]:
						opt2 = False
					l_aux += 1
					r_aux -= 1
				return opt1 or opt2

			l += 1
			r -= 1
		return True