
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution:
	# O(n) time, O(n) space
	def numSplits(self, s: str) -> int:
		def distinct_letters(string):
			letters, counter, ans = set(), 0, [0] * len(string)
			for i in range(len(string)):
				if string[i] not in letters:
					counter += 1
					letters.add(string[i])
				ans[i] = counter
			return ans

		# prefix[i] = # distinct letters in s[:i + 1]
		prefix = distinct_letters(s)

		#  sufix[i] = # distinct letters in s[i:]
		sufix = distinct_letters(s[::-1])
		sufix = sufix[::-1]

		num_good_partitions = 0
		for i in range(len(prefix) - 1):
			if prefix[i] == sufix[i + 1]:
				num_good_partitions += 1

		return num_good_partitions