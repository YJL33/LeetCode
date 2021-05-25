"""
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dmy = ListNode(0)
        cur, s = dmy, 0

        while l1 or l2:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next, s = ListNode(s%10), s/10
            l1, l2, cur = l1.next if l1 else l1, l2.next if l2 else l2, cur.next

        if s != 0: cur.next = ListNode(s)
        return dmy.next
