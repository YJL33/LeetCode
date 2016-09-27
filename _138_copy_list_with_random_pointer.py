"""
138. Copy List with Random Pointer

    Total Accepted: 76899
    Total Submissions: 293335
    Difficulty: Hard

A linked list is given such that each node contains an additional random pointer,
which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None

        # original: A->B->C->D
        # 1. copy:     A->A'->B->B'->C->C'->D->D'
        # 2. random:   A'.random = A.random.next
        # 3. extract copy

        dmy = RandomListNode(0)
        dmy.next = head

        # step 1
        while head:
            nexthead = head.next
            copy = RandomListNode(head.label)
            head.next = copy
            copy.next = nexthead
            head = nexthead

        # step 2
        head = dmy.next
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

        # step 3
        dmy2 = RandomListNode(0)
        cpy, cur = dmy2, dmy.next

        while cur:
            nextcur = cur.next.next
            cpy.next = cur.next         # extract the copy
            cpy = cpy.next
            cur.next = nextcur          # restore the original
            cur = cur.next

        return dmy2.next