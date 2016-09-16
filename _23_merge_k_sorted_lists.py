"""
23. Merge k Sorted Lists

    Total Accepted: 103356
    Total Submissions: 416913
    Difficulty: Hard

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its comleftexity.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        if len(lists) == 0: return None;
        if len(lists) == 1: return lists[0];
        else:
            mid = len(lists)//2;
            left = self.mergeKLists(lists[0:mid]);
            right = self.mergeKLists(lists[mid:]);

            p = dummy;
            while left != None or right != None:
                if right == None or (left != None and left.val <= right.val):
                    p.next = ListNode(left.val);
                    left = left.next;
                else:
                    p.next = ListNode(right.val);
                    right = right.next;
                p = p.next;

            return dummy.next;

    def mergeKLists2(self, lists):
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next