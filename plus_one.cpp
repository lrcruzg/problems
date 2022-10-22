#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/plus-one/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(digits)
	vector<int> plusOne(vector<int>& digits) {
		bool carry = true;

		for(int i = digits.size() - 1; i >= 0; --i) {
			if(carry)
				++digits[i];

			digits[i] %= 10;
			carry = carry and digits[i] == 0;
		}

		if(digits[0] == 0)
			digits.insert(digits.begin(), 1);

		return digits;
	}
};
