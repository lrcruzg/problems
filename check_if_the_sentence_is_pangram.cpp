#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(sentence)
	bool checkIfPangram(string sentence) {
		vector<int> freq(26);
		
		for(auto c : sentence)
			++freq[c - 'a'];
		
		return *min_element(freq.begin(), freq.end()) >= 1;
	}
};
