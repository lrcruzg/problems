from typing import Optional, Tuple
from ListNode_util import *

# https://leetcode.com/problems/sort-list/

class Solution:
	# O(nlog(n)) time.
	# O(log(n)) space (recursion stack).
	# where n = number of nodes in the list.
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if(not head or not head.next):
			return head

		l1, l2 = self.split(head)

		l1 = self.sortList(l1)
		l2 = self.sortList(l2)

		dummy_head = ListNode(-1, None)
		it = dummy_head

		# merge the sorted list
		while l1 and l2:
			if l1.val < l2.val:
				it.next = l1
				l1 = l1.next
			else:
				it.next = l2
				l2 = l2.next
			it = it.next

		if l1:
			it.next = l1
		else: 
			it.next = l2

		return dummy_head.next

	# O(n) time, O(1) space.
	def split(self, head: ListNode) -> Tuple[ListNode]:
		dummy_head = ListNode(-1, head)
		slow = dummy_head
		fast = dummy_head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next
			if fast:
				fast = fast.next

		mid = slow.next
		slow.next = None

		return head, mid
