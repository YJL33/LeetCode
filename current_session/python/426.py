"""
426

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

Think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list.
For a circular doubly linked list, the predecessor of the first element is the last element,
and the successor of the last element is the first element.

We want to do the transformation in place.
After the transformation, the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor.

You should return the pointer to the smallest element of the linked list.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # in-order traverse
        # tc: O(n)
        # sc: O(n)
        # recursion
        if not root: return

        self.visit = []

        def helper(node):
            if not node: return
            helper(node.left)
            self.visit.append(node)
            helper(node.right)
            return
        
        helper(root)
        N = len(self.visit)
        for i, n in enumerate(self.visit):
            n.left = self.visit[(i-1)%N]
            n.right = self.visit[(i+1)%N]
        
        return self.visit[0]

    def treeToDoublyList_iterative(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # in-order traverse (iterative)
        # keep adding parent node into stack and visit left child
        # see more at binary tree review document
        # tc: O(n) to visit all nodes
        # sc: O(1) if modify in-place, O(h) for recursive stack
        if not root: return

        dummy = Node(0)

        stack, node, prev = [], root, dummy

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right

        dummy.right.left, prev.right = prev, dummy.right

        return dummy.right

    def treeToDoublyList_recursive(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # in-order traverse recursive
        # tc: O(n) to visit all nodes
        # sc: O(1) if modify in-place, O(h) for recursive stack
        if not root: return

        dummy = Node(0)

        def helper(node, prev):
            if not node: return
            left_last = helper(node.left, prev) or prev
            left_last.right, node.left = node, left_last
            right_last = helper(node.right, node)                     # handle the right sub-bst
            return right_last or node
        
        last = helper(root, dummy)
        
        head = dummy.right
        head.left, last.right = last, head
        del dummy
        
        return head