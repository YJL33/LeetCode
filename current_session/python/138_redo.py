"""
see https://leetcode.com/problems/copy-list-with-random-pointer/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # create a dictionary: key=node.val val=node
        # step 1: create nodes with next pointer
        # step 2: when creating, add each node into dict: k=node.val, v=node
        # step 3: for all nodes (iterate with next), assign random
        
        # 1
        dh, p1 = Node(0), head
        p2 = dh
        od, nd, i = {}, {}, 0
        while p1:
            p2.next = Node(p1.val)
            nd[i], od[p1] = p2.next, i
            p1, p2, i = p1.next, p2.next, i+1       # 2

        p3, p4 = head, dh.next
        while p3:                                   # 3
            if p3.random != None:
                p4.random = nd[od[p3.random]]
            p3, p4 = p3.next, p4.next

        return dh.next
        