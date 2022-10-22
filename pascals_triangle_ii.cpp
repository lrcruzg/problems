#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/pascals-triangle-ii/

class Solution {
public:
	// O(n) time.
	// O(1) space (solution space is not considered).
	// where n = rowIndex.
	vector<int> getRow(int rowIndex) {
		vector<int> ans(rowIndex + 1);
		ans[0] = 1;

		int prev_val = 0;
		int tmp;

		for(int i = 0; i < ans.size(); ++i) {
			prev_val = 0;
			for(int j = 0; j < i + 1; ++j) {
				tmp = ans[j];
				ans[j] = prev_val + ans[j];
				prev_val = tmp;
			}
		}

		return ans;
	}
};
