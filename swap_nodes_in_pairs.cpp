#include <bits/stdc++.h>
#include "ListNode_util.h"
using namespace std;

// https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution {
public:
	// O(n) time.
	// O(n) space (recursion stack).
	// where n = number of nodes in the list.
	ListNode* swapPairs(ListNode* head) {
		if(!head || !head->next)
			return head;

		ListNode* next_pair_head = head->next->next;

		ListNode* new_head = head->next;
		new_head->next = head;

		head->next = swapPairs(next_pair_head);

		return new_head;
	}
};
