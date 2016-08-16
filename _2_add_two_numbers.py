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
        dummyhead = ListNode(0)
        prev = dummyhead
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val         # get the value
                l1 = l1.next            # and move on
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry%10)
            prev = prev.next
            carry //= 10                # carry to next digit

        return dummyhead.next