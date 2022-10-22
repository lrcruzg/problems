#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/merge-sorted-array/

class Solution {
public:
	// O(m + n) time.
	// O(1) space.
	// where m = len(nums1), n = len(nums2)
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		while(m && n) {
			if(nums1[m - 1] < nums2[n - 1]) {
				nums1[m + n - 1] = nums2[n - 1];
				--n;
			} else {
				nums1[m + n - 1] = nums1[m - 1];
				--m;
			}
		}

		while(n) {
			nums1[n - 1] = nums2[n - 1];
			--n;
		}
	}
};
