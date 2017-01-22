"""
369. Plus One Linked List

    Total Accepted: 5079
    Total Submissions: 9876
    Difficulty: Medium

Given a non-negative number represented as a singly linked list of digits,
plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Example:        Input: 1->2->3   =>   Output: 1->2->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur, number, count = head, head, 0, 0
        while cur:
            prev, cur, number, count = cur, cur.next, 10*number+cur.val, count+1
        number += 1

        digits = []
        while number:
            digits += number%10,
            number = number/10            

        cur = head
        for i in xrange(count):
            cur.val, cur = digits[::-1][i], cur.next

        if count < len(digits):
            prev.next = ListNode(digits[0])

        return head
