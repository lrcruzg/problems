#include <bits/stdc++.h>
#include "TreeNode_util.h"
using namespace std;

// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class Solution {
public:
	// O(n) time.
	// O(h) space.
	// where n = number of nodes, 
	// h = height of the tree.
	int sumRootToLeaf(TreeNode* root) {
		return aux(root, 0);
	}

	int aux(TreeNode* node, int c_num) {
		if(not node)
			return 0;

		int new_c_num = (c_num << 1) | node->val;

		if(not node->left and not node->right)
			return new_c_num;

		return aux(node->left, new_c_num)
				+ aux(node->right, new_c_num);
	}
};
