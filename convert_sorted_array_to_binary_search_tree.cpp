#include <bits/stdc++.h>
#include "TreeNode_util.h"
using namespace std;

// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class Solution {
public:
	// O(n) time.
	// O(log(n)) space (recursion stack).
	// where n = len(nums)
	TreeNode* sortedArrayToBST(vector<int>& nums) {
		return aux(nums, 0, nums.size() - 1);
	}

	TreeNode* aux(vector<int>& nums, int l, int r) {
		if(r < l)
			return nullptr;

		int mid = l + (r - l) / 2;
		TreeNode* node = new TreeNode(nums[mid]);
		node->left = aux(nums, l, mid - 1);
		node->right = aux(nums, mid + 1, r);

		return node;
	}
};
