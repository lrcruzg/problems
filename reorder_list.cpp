#include <bits/stdc++.h>
#include "ListNode_util.h"
using namespace std;

// https://leetcode.com/problems/reorder-list/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = number of nodes in the list.
	void reorderList(ListNode* head) {
		auto[it_head, it_mid] = split_middle(head);
		it_mid = reverse(it_mid);
		ListNode* aux_head;
		ListNode* aux_mid;

		while(it_head and it_mid) {
			aux_head = it_head->next;
			aux_mid = it_mid->next;

			it_head->next = it_mid;
			it_mid->next = aux_head;

			it_head = aux_head;
			it_mid = aux_mid;
		}
	}

	pair<ListNode*, ListNode*> split_middle(ListNode* head) {
		ListNode* dummy = new ListNode(-1, head);

		ListNode* slow = dummy;
		ListNode* fast = dummy;

		while(fast and fast->next) {
			slow = slow->next;
			fast = fast->next;
			if(fast)
				fast = fast->next;
		}

		ListNode* mid = slow->next;
		slow->next = nullptr;

		delete dummy;

		return {head, mid};
	}

	ListNode* reverse(ListNode* head) {
		ListNode* rev_head = nullptr;
		ListNode* it = head;
		ListNode* aux;

		while(it) {
			aux = it;
			it = it->next;
			aux->next = rev_head;
			rev_head = aux;
		}

		return rev_head;
	}
};
