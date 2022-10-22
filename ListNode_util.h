#include <iostream>
#include <vector>

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
};

/**
 * @brief Creates a list using the elements of the vector.
 * 
 * @param nums vector whose elements will be the values of the nodes in the list.
 * @return ListNode* head adress of the list.
 */
ListNode* vector_to_listnode(std::vector<int>& nums) {
	ListNode* dummy_head = new ListNode(-1);
	ListNode* it = dummy_head;
	for(const auto n: nums) {
		it->next = new ListNode(n);
		it = it->next;
	}

	ListNode* head = dummy_head->next;
	delete dummy_head;
	
	return head;
}

/**
 * It's assumed that there isn't cycles in the list.
 */
std::ostream& operator<<(std::ostream& out, const ListNode* list) {
	while(list) {
		out << list->val << " -> ";
		list = list->next;
	}

	return out;
}