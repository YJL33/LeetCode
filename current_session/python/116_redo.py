# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections

# use queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        dh = Node(0)
        dh.next = root
        # use queue / bfs
        dq = collections.deque()
        dq.append(root)
        prev = None
        nextLayer = collections.deque()

        while dq:
            currentNode = dq.popleft()
            if prev: prev.next = currentNode
            prev = currentNode
            if currentNode.left:
                nextLayer.append(currentNode.left)
            if currentNode.right:
                nextLayer.append(currentNode.right)
            if len(dq) == 0:
                dq = nextLayer
                nextLayer = collections.deque()
                prev = None
        
        return dh.next