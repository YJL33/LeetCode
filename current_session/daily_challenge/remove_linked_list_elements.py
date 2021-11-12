# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        dummyHead = ListNode(0)
        prev, cur, dummyHead.next = dummyHead, head, head
        while cur:
            while cur and cur.val == val:
                cur = cur.next
            prev.next, prev, cur = cur, cur, cur.next
        return dummyHead.next