
# https://leetcode.com/problems/find-the-difference/

class Solution:
	# O(n) time.
	# O(1) space.
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s:
            ans ^= ord(c)
            
        for c in t:
            ans ^= ord(c)
        
        return chr(ans)
