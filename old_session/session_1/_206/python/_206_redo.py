"""
 206. Reverse Linked List

    Total Accepted: 190682
    Total Submissions: 434361
    Difficulty: Easy
    Contributors: Admin

Reverse a singly linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = None, head
        while cur:
            new = cur.next
            cur.next = prev
            prev = cur
            cur = new
        return prev
