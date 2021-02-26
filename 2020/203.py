"""
203
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dh = ListNode(0)
        prev, cur, dh.next = dh, head, head

        while cur:
            if cur.val == val:
                prev.next, cur = cur.next, cur.next
            else:
                prev, cur = cur, cur.next
        
        return dh.next