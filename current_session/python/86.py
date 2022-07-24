# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        dh, tmp, cur = left, right, head
        while cur:
            if cur.val >= x:
                right.next, right = cur, cur
            else:
                left.next, left = cur, cur
            cur = cur.next
        left.next, right.next = tmp.next, None
        return dh.next