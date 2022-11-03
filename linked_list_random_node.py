from typing import Optional
from ListNode_util import *

# https://leetcode.com/problems/linked-list-random-node/

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size = self.get_size()
    
    # O(n) time, O(1) space
    def get_size(self):
        n = 0
        it = self.head
        while it:
            n += 1
            it = it.next
        
        return n

    # O(n) time.
    # O(1) space.
    # where n = number of nodes in the list
    def getRandom(self) -> int:
        r = random.randint(0, self.size - 1)
        it = self.head
        while r:
            it = it.next
            r -= 1
        
        return it.val
