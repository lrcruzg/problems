from typing import List

# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
	# O(nlog(n)) time.
	# O(1) space.
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(2, len(arr)):
            if arr[1] - arr[0] != arr[i] - arr[i - 1]:
                return False
        
        return True
