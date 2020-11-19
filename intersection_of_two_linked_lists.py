
# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# O(m + n) time, O(1) space
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		if not headA or not headB: return None
		lenA, lastA = self.length_and_last(headA)
		lenB, lastB = self.length_and_last(headB)
		if lastA != lastB: return None
		hA, hB = headA, headB
		while hA != hB:
			if lenB < lenA:
				hA = hA.next
				lenA -= 1
			elif lenA < lenB:
				hB = hB.next
				lenB -= 1
			else:
				hA = hA.next
				hB = hB.next
		return hB


	def length_and_last(self, head):
		l = 0
		while head:
			l += 1
			if not head.next:
				last = head
			head = head.next
		return (l, last)