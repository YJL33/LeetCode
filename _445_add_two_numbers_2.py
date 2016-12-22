"""
 445. Add Two Numbers II

    Total Accepted: 4547
    Total Submissions: 10202
    Difficulty: Medium
    Contributors: Admin

You are given two linked lists representing two non-negative numbers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
        n1, n2 = 0, 0
        while l1:
            n1 = 10*n1+l1.val
            l1 = l1.next

        while l2:
            n2 = 10*n2+l2.val
            l2 = l2.next

        res = n1+n2
        prev, cur = None, None

        while res:
            n, res = res%10, res//10
            cur = ListNode(n)
            cur.next = prev
            prev = cur

        return cur or [0]