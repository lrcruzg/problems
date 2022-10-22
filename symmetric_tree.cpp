#include <bits/stdc++.h>
#include "TreeNode_util.h"
using namespace std;

// https://leetcode.com/problems/symmetric-tree/

class Solution {
public:
	// O(n) time.
	// O(h) space (recursion stack).
	// where n = number of nodes in the tree, h = head of the tree.
	bool isSymmetric(TreeNode* root) {
		return are_symmetric(root->left, root->right);
	}

	bool are_symmetric(TreeNode* a, TreeNode* b) {
		if(!a || !b)
			return a == b;

		return a->val == b->val && are_symmetric(a->left, b->right) && are_symmetric(a->right, b->left);
	}
};
