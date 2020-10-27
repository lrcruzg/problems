
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    # O(len(s)) time, O(1) space
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        counter = 0
        for i in s:
            if i == "(":
                counter += 1
            elif i == ")":
                counter -= 1
            max_depth = max(max_depth, counter)
        return max_depth