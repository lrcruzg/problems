#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution {
public:
	// O(n) time.
	// O(1) space (27 lowercase letters).
	int firstUniqChar(string s) {
		int fst_unique_idx = -1;
		vector<int> char_freq(26);

		for(char c : s)
			++char_freq[c - 'a'];

		for(int i = 0; i < s.size(); ++i) {
			if(char_freq[s[i] - 'a'] == 1) {
				fst_unique_idx = i;
				break;
			}
		}

		return fst_unique_idx;
	}
};
