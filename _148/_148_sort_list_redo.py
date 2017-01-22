"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # implement mergesort
        if not head or not head.next: return head
        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        # after this line, we have two sublist beginning with head and slow
        return self.merger(self.sortList(head), self.sortList(slow))

    def merger(self, ha, hb):
        dummy = ListNode(0)
        cursor = dummy
        while ha and hb:
            if ha.val <= hb.val:
                cursor.next, cursor, ha = ha, ha, ha.next   # first cursor.next, then cursor
            else:
                cursor.next, cursor, hb = hb, hb, hb.next
        cursor.next = ha or hb
        return dummy.next
