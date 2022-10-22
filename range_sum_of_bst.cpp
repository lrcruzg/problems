#include <iostream>
#include "TreeNode_util.h"

// https://leetcode.com/problems/range-sum-of-bst/

class Solution {
public:
	// O(n) time.
	// O(h) space (recursion stack)
	// where n = number of nodes in the tree, 
	// h = height of the tree.
	int rangeSumBST(TreeNode* root, int low, int high) {
		if(not root)
			return 0;

		if(high < root->val)
			return rangeSumBST(root->left, low, high);

		if(root->val < low)
			return rangeSumBST(root->right, low, high);

		return root->val + rangeSumBST(root->left, low, high) 
						 + rangeSumBST(root->right, low, high);
	}
};
