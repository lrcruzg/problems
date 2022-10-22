#include <bits/stdc++.h>
#include "TreeNode_util.h"
using namespace std;

// https://leetcode.com/problems/same-tree/

class Solution {
public:
	// O(max(n,m)) time.
	// O(max(h_n, h_m)) space (rec. stack).
	// where n = number of nodes in p, m = number of node in q
	// and h_n = height of p, h_m = height of q.
	bool isSameTree(TreeNode* p, TreeNode* q) {
		if(!p || !q)
			return p == q;

		return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
	}
};
