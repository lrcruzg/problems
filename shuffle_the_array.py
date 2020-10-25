
# https://leetcode.com/problems/shuffle-the-array/

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        aux = nums.copy()
        i, j = 0, n
        k = 0
        while i < n:
            nums[k] = aux[i]
            nums[k + 1] = aux[j]
            i += 1
            j += 1
            k += 2
        return nums