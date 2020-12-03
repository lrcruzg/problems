
# https://leetcode.com/problems/valid-palindrome/

class Solution:
	# O(n) time, O(1) space
	def isPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1
		alphanum = {"q","w","e","r","t","y","u","i","o","p","a","s"
				,"d","f","g","h","j","k","l","ñ","z","x","c","v"
				,"b","n","m","1","2","3","4","5","6","7","8","9","0"}
		while l < r:
			if s[l].lower() not in alphanum:
				l += 1

			elif s[r].lower() not in alphanum:
				r -= 1
			else:
				if s[l].lower() != s[r].lower():
					return False
				else:
					l += 1
					r -= 1
		return True