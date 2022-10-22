#include <bits/stdc++.h>
#include "ListNode_util.h"
using namespace std;

// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = number of nodes in the list.
	ListNode* deleteMiddle(ListNode* head) {
		if(!head->next) return nullptr;

		ListNode* mid = middleNode(head);
		ListNode* it = head;

		while(it->next != mid)
			it = it->next;

		it->next = it->next->next;

		return head;
	}

	ListNode* middleNode(ListNode* head) {
		ListNode* slow = head;
		ListNode* fast = head->next;

		while(fast) {
			slow = slow->next;
			fast = fast->next;
			if(fast)
				fast = fast->next;
		}

		return slow;
	}
};
