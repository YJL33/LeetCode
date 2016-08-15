"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Step through the listnode with fast(2) and slow(1) steps, meanwhile reverse slow steps
        # when fast reach end, slow is the middle point.
        # Compare each element in both part are same or not, and restore the listnode.
        # e.g.         A -> B -> B -> A -> (x)
        #       (x) <- A <- B    B -> A -> (x)
        rev = None
        fast = slow = head
        while fast and fast.next:                           # not reach the end yet
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next      # reverse 1st half
        # after this line, it become 2 parts, beginning with slow and rev
        junction = slow                                     # record where list-node aparts
        if fast:
            slow = slow.next

        res = True
        while rev:
            res = res and (rev.val == slow.val)     # check whether it's palindrome or not
            junction, rev.next, rev = rev, junction, rev.next       # restore the list
            slow = slow.next                                        # keep progress

        return res