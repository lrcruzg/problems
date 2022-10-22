#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/shifting-letters/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	string shiftingLetters(string s, vector<int>& shifts) {
		shifts[shifts.size() - 1] %= 26;

		for(int i = shifts.size() - 2; i >= 0; --i)
			shifts[i] = (shifts[i] + shifts[i + 1]) % 26;

		for(int i = 0; i < shifts.size(); ++i)
			s[i] = ((s[i] + shifts[i] - 'a') % 26) + 97;

		return s;
	}
};
