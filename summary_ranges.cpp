#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/summary-ranges/

class Solution {
public:
	// O(n) time.
	// O(1) space (solution space is not considered).
	// where n = len(nums).
	vector<string> summaryRanges(vector<int>& nums) {
		if(nums.empty()) return {};
		
		vector<string> ranges;
		string c_range;
		int start = 0;
		for(int i = 1; i < nums.size(); ++i) {
			if(nums[i] != nums[i - 1] + 1) {
				if(start != i - 1) {
					c_range = to_string(nums[start]) + "->" + to_string(nums[i - 1]);
				} else {
					c_range = to_string(nums[start]);
				}

				ranges.push_back(c_range);
				start = i;
			}
		}

		if(start != nums.size() - 1) {
			ranges.push_back(to_string(nums[start]) + "->" + to_string(nums[nums.size() - 1]));
		} else {
			ranges.push_back(to_string(nums[start]));
		}

		return ranges;
	}
};
