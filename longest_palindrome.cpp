#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/longest-palindrome/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(s).
	int longestPalindrome(string s) {
		int even_oc = 0;
		int odd_oc = 0;
		int num_odd_chars = 0;

		vector<int> char_cntr(256);

		for(char c : s)
			++char_cntr[int(c)];

		for(int n : char_cntr) {
			if(n % 2 == 0) {
				even_oc += n;
			} else {
				++num_odd_chars;
			}
		}

		if(num_odd_chars)
			odd_oc = s.size() - even_oc - (num_odd_chars - 1);

		return even_oc + odd_oc;
	}
};
