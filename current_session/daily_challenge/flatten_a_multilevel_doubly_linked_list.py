# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':        
        # edge case
        if not head: return

        # use stack
        stack = [head]
        prev = None

        while stack:
            node = stack.pop()
            # print('prev:', prev.val if prev else "none", 'node:', node.val)
            node.prev = prev
            if prev: prev.next = node
            # keep going until we met some node has child
            while node and node.child == None:
                prev, node = node, node.next
            # we met a node has child
            if node != None:
                if node.next:
                    # print('stack+', node.next.val)
                    stack.append(node.next)
                x = self.flatten(node.child)
                node.child, node.next, x.prev = None, x, node
                if not prev: prev = head                        # edge case: prev is None, node is head
                while prev and prev.next: prev = prev.next

        return head