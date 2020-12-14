
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List
import heapq

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next	

class Solution:
	# O(nlog(k)) time, O(n) space
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		ListNode.__lt__ = lambda self, other: self.val < other.val
		heap = []
		head = ListNode(0)
		aux = head

		for node in lists:
			if node:
				heapq.heappush(heap, node)

		while heap:
			current_minimum = heapq.heappop(heap)
			if current_minimum.next:
				heapq.heappush(heap, current_minimum.next)
			aux.next = ListNode(current_minimum.val)
			aux = aux.next

		return head.next


	'''
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		if len(lists) == 0: return None
		if len(lists) == 1: return lists[0]
		return self.merge(self.mergeKLists(lists[:len(lists) // 2])
						, self.mergeKLists(lists[len(lists) // 2:]))

	def merge(self, l1, l2):
		if not l1: return l2
		if not l2: return l1
		if l1.val < l2.val:
			l1.next = self.merge(l1.next, l2)
			return l1
		l2.next = self.merge(l1, l2.next)
		return l2
	'''