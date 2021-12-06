# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use tortuise-hare algorighm
        dh = ListNode(0)
        dh.next = head
        fast, slow = dh
        prev = slow
        while fast.next and fast.next.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        # now slow is at middle
        prev.next = slow.next
        return dh.next
