# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional
import collections
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use dict
        node_dict = collections.defaultdict(int)
        cur, i = head, 0
        while cur:
            if cur not in node_dict:
                node_dict[cur] = i
                i += 1
                cur = cur.next
            else:
                return cur
        return
    
    def detectCycle_O1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use turtoise-hare algorithm
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        
        if not fast or not fast.next: return None

        cur = head
        while cur != slow:
            cur, slow = cur.next, slow.next
        
        return cur