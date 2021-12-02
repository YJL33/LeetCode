# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dh = ListNode(0)
        dh.next = head
        prev, oddCur = head, head

        even = ListNode(0)
        evenCur = even

        while oddCur and evenCur:
            prev = oddCur
            evenCur.next = oddCur.next
            evenCur = evenCur.next

            if evenCur:
                oddCur.next = evenCur.next
                oddCur = oddCur.next
        
        prev.next = even.next
        
        return dh.next