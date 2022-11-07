#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/maximum-subarray/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(nums).
	int maxSubArray(vector<int>& nums) {
		int max_sum = nums[0], dp = 0;
		for(auto n : nums) {
			dp = max(n, dp + n);
			max_sum = max(dp, max_sum);
		}
		return max_sum;
	}
};