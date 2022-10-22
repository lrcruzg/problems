#include <bits/stdc++.h>
using namespace std;

// https://leetcode.com/problems/copy-list-with-random-pointer/

class Node {
public:
	int val;
	Node* next;
	Node* random;
	
	Node(int _val) {
		val = _val;
		next = NULL;
		random = NULL;
	}
};

class Solution {
public:
	// O(n) time.
	// O(n) space.
	// where n = number of nodes in the list.
	Node* copyRandomList(Node* head) {
		// copy the list structure
		Node* dummy_head = new Node(-1);
		Node* it = head;
		Node* it_copy = dummy_head;

		map<Node*, Node*> node_to_copy;
		node_to_copy[nullptr] = nullptr;

		// copy list without random pointer
		while(it) {
			it_copy->next = new Node(it->val);
			it_copy = it_copy->next;
			node_to_copy[it] = it_copy;
			it = it->next;
		}

		Node* copy_head = dummy_head->next;
		delete dummy_head;

		// set the random pointers
		it = head;
		it_copy = copy_head;
		while(it) {
			it_copy->random = node_to_copy[it->random];
			it_copy = it_copy->next;
			it = it->next;
		}

		return copy_head;
	}
};
