"""
see https://leetcode.com/problems/merge-two-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        cur = dummyHead
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next

        while l1:
            cur.next = l1
            cur = l1
            l1 = l1.next
        while l2:
            cur.next = l2
            cur = l2
            l2 = l2.next

        return dummyHead.next