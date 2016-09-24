"""
25. Reverse Nodes in k-Group

    Total Accepted: 70356
    Total Submissions: 243535
    Difficulty: Hard

Given a linked list,
reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k,
then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes,
only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # similar to #19, get a specific length (k) first
        if not head: return []
        if k == 1: return head

        dmy = ListNode(0)
        dmy.next, prev, cur = head, dmy, self.moveKstep(head, k)
        #print prev.val, head.val, cur.val
        while self.hasNext(head, k):
            self.reverser(prev, head, cur)
            head, prev, cur = cur, self.moveKstep(prev, k), self.moveKstep(cur, k)
        return dmy.next

    def hasNext(self, cur, k):
        # QUITE UGLY HERE!!!!
        step = 0
        while step < k and cur:
            step, cur = step+1, cur.next
        return step == k

    def moveKstep(self, cur, k):
        # check whether we can reverse or not
        step = 0
        while step < k and cur:
            step, cur = step+1, cur.next
        return cur

    def reverser(self, prev, head, tail):
        # reverse listnodes in between
        # Iterative method, T:O(n), S:O(1)
        last, back = head, tail
        while head != tail:
            head, last = head.next, head
            last.next, back = back, last
        prev.next = last