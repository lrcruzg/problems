#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(nums).
	int removeDuplicates(vector<int>& nums) {	
		int last_index = 0;
		for(int i = 1; i < nums.size(); ++i) {
			if(nums[i] != nums[last_index])
				nums[++last_index] = nums[i];
		}

		return ++last_index;
	}
};
