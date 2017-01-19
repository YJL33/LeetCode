"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dmy = ListNode(0)
        cur = dmy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
                cur = cur.next
            else:
                cur.next, l2 = l2, l2.next
                cur = cur.next
        # here one of them is None, and cur needs to hook to the other one.
        cur.next = l1 if l1 is not None else l2
        return dmy.next
