"""
117
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # handle layer by layer
        if not root: return root
        dh = Node(0)
        dh.next = root
        root.next = None
        stack = [root]
        while stack:
            # tail the nodes within the same layer
            # add next layer
            tmp = []
            for n in stack:
                if n.left: tmp += n.left,
                if n.right: tmp += n.right,
            nxt = None
            while stack:
                x = stack.pop()
                x.next = nxt
                nxt = x
            stack = tmp
        return dh.next
