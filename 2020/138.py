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
        # 1st stage: go through the whole old list
        #            store the corresponding position for each old node
        # 2nd stage: go thorugh the whole old list
        #            create new node and its next
        #            store the corresponding position for each new node
        #            STORE THE RANDOM'S OLD POSITION IF ANY
        # 3nd stage: point to its random to the corresponding position

        dmy = Node(0)
        p1, i = head, 0
        oldPos = {}                     # old node -> position
        while p1:
            oldPos[p1] = i
            p1, i = p1.next, i+1
        
        p2, cur, j = head, dmy, 0
        rnd = {}                        # key: new node,  val: random's position
        newPos = [0 for _ in range(i)]  # position -> new node
        while p2:
            cur.next = Node(p2.val)     # create new node
            cur = cur.next
            newPos[j] = cur             # store new node in its position
            if p2.random:
                rnd[cur] = oldPos[p2.random]       # use its old position
            p2, j = p2.next, j+1
        
        p3 = dmy.next
        while p3:
            if p3 in rnd:
                p3.random = newPos[rnd[p3]]
            p3 = p3.next
            
        return dmy.next