
# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
	# O(n + m) time
	# O(n + m) space (solution space)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += (word1[i] + word2[i])
        
        if len(word1) <= len(word2):
            res += word2[len(word1):]
        else:
            res += word1[len(word2):]
        
        return res
