"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # naive approach
        dh = ListNode(0)
        dh.next = head

        # go to m
        prev, cur, pos = dh, head, 1
        while pos < m:
            prev, cur, pos = cur, cur.next, pos+1

        # go to n while reversing it
        tail = cur
        nxt = cur.next
        while pos < n:
            tmp = nxt.next
            nxt.next, cur = cur, nxt
            nxt = tmp
            pos += 1

        # hook it up
        prev.next = cur
        tail.next = nxt

        return dh.next