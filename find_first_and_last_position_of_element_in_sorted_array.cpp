#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution {
public:
	// O(log(n)) time.
	// O(1) space.
	// where n = len(nums).
	vector<int> searchRange(vector<int>& nums, int target) {
		if(nums.size() == 0) return {-1, -1};

		int l = 0, r = nums.size() - 1, mid;
		int fst = 0, lst = 0;

		// Binary Search for the first occurrence
		while(l <= r) {
			mid = l + (r - l) / 2;
			if(target <= nums[mid]) {
				fst = mid;
				r = mid - 1;
			}
			else {
				l = mid + 1;
			}
		}

		// Binary Search for the last occurrence
		l = 0, r = nums.size() - 1;
		while(l <= r) {
			mid = l + (r - l) / 2;
			if(nums[mid] <= target) {
				lst = mid;
				l = mid + 1;
			}
			else {
				r = mid - 1;
			}
		}

		if(nums[fst] != target)
			return {-1, -1};

		return {fst, lst};
	}
};