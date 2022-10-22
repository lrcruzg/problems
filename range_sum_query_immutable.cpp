#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray {
public:
	vector<int> pref_sums;

	NumArray(vector<int>& nums) {
		pref_sums.assign(nums.size() + 1, 0);

		for(int i = 0; i < nums.size(); ++i) {
			pref_sums[i + 1] = pref_sums[i] + nums[i];
		}
	}
	
	int sumRange(int left, int right) {
		return pref_sums[right + 1] - pref_sums[left];
	}
};
