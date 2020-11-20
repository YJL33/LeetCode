"""
https://leetcode.com/problems/sort-list/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # implement merge sort
        if not head or not head.next: return head
        dh = ListNode(0)
        dh.next = head
        prev, fast, slow = None, head, head
        while fast and fast.next:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        # now we can 
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        dh = ListNode(0)
        cur = dh

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next

        cur.next = l1 or l2
        return dh.next
