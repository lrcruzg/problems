#include <bits/stdc++.h>
#include "ListNode_util.h"
using namespace std;

// https://leetcode.com/problems/partition-list/

class Solution {
public:
	// O(n) time.
	// O(1) space.
	// where n = number of nodes in the list.
	ListNode* partition(ListNode* head, int x) {
		ListNode* less_head = new ListNode(-1);
		ListNode* geq_head = new ListNode(-1);
		
		ListNode* less_it = less_head;
		ListNode* geq_it = geq_head;

		ListNode* it = head;

		while(it) {
			if(it->val < x) {
				less_it->next = it;
				less_it = less_it->next;
			} 
			else {
				geq_it->next = it;
				geq_it = geq_it->next;
			}

			it = it->next;
		}

		geq_it->next = nullptr;
		less_it->next = geq_head->next;

		ListNode* new_head = less_head->next;

		delete less_head;
		delete geq_head;

		return new_head;
	}
};
