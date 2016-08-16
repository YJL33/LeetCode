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
    def merger(self, h1, h2):
        # merge two list
        dummy = ListNode(0)
        cursor = dummy
        while h1 and h2:
            if h1.val > h2.val:
                cursor.next, cursor, h2 = h2, h2, h2.next
            else:
                cursor.next, cursor, h1 = h1, h1, h1.next
        cursor.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # implement mergesort:
        # cut to half => sort the 1st half => sort the 2nd half => merge together
        if not head or not head.next:
            return head
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        # Now we have two small list, init by head and slow

        return self.merger(*map(self.sortList, (head, slow)))       # most delicate part
        # Recursion => Time: O(n), Space: O(logn)