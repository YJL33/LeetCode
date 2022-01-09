# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.nd = {}
        cur, i = self.head, 1
        while cur:
            self.nd[i] = cur
            cur, i = cur.next, i+1
        self.L = min(10000, i)

    def getRandom(self) -> int:
        # since the number of nodes in list will be within [1,10000]
        # simply generate a number b/w these and get the node
        i = random.randint(1,self.L)
        return self.nd[i].val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()