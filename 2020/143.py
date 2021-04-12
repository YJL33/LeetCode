"""
143
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node: ListNode) -> None:
        prev = None
        while node and node.next:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        node.next = prev
        return node         

    def zipList(self, l, r):
        dmy = ListNode(0)
        cur = dmy
        while l and r:
            a, b = l.next, r.next
            cur.next = l
            cur.next.next = r
            r.next = None
            cur, l, r = cur.next.next, a, b
        if l:
            cur.next = l
            # assert(l.next == None)
        return dmy.next

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        if not head.next or not head.next.next: return head
        dh = ListNode(0)
        dh.next = head

        # reverse the bottom half, and zip them together
        slow, fast = head.next, head.next.next
        while slow.next and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # print('slow, fast', slow, fast)
        
        l, r = dh.next, self.reverse(slow.next)
        slow.next = None
        # print('l, r', l, r)

        # zip them together
        return self.zipList(l, r)