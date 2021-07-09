"""
https://leetcode.com/problems/add-two-numbers-ii/
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNum(n):
            ans = 0
            while n:
                ans = 10*ans+n.val
                n = n.next
            return ans

        def getListNode(num):
            if num == 0:
                return ListNode(0)
            stack = []
            while num:
                stack += num%10,
                num = num//10
            dh = ListNode(0)
            prev = dh
            while stack:
                prev.next = ListNode(stack.pop())
                prev = prev.next
            return dh.next

        n1 = getNum(l1)
        n2 = getNum(l2)
        return getListNode(n1+n2)