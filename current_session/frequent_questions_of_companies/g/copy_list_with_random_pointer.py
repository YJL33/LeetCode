class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # use dict: key=old node, value=copied node
        # create copy of list first
        dummyHead = Node(0)
        copy, cur = dummyHead, head
        nodeDict = {}
        while cur:
            copy.next = Node(cur.val)
            nodeDict[cur] = copy.next
            copy, cur = copy.next, cur.next
        
        # copy random
        c1, c2 = head, dummyHead.next
        while c2:
            if c1.random: c2.random = nodeDict[c1.random]
            c1, c2 = c1.next, c2.next
        
        return dummyHead.next
