#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = len(s).
	string reverseVowels(string s) {
		int l = 0, r = (int)s.size() - 1;

		while(l < r) {
			if(!is_vowel(s[l])) ++l;
			else if(!is_vowel(s[r])) --r;
			else {
				swap(s[l], s[r]);
				++l; --r;
			}
		}

		return s;
	}

	bool is_vowel(char c) {
		return c == 'a' 
			|| c == 'e' 
			|| c == 'i' 
			|| c == 'o' 
			|| c == 'u' 
			|| c == 'A' 
			|| c == 'E' 
			|| c == 'I' 
			|| c == 'O' 
			|| c == 'U';
	}
};
