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
        cur, carry = dmy, 0

        while l1 and l2:
            cur.next = ListNode((l1.val+l2.val+carry)%10)
            carry = 1 if (l1.val+l2.val+carry) > 9 else 0
            l1, l2, cur = l1.next, l2.next, cur.next

        remain = l1 if (not l2) else l2
        while remain:
            cur.next = ListNode((remain.val+carry)%10)
            carry = 1 if (remain.val+carry) > 9 else 0
            remain, cur = remain.next, cur.next

        if carry != 0: cur.next = ListNode(carry)
        return dmy.next
