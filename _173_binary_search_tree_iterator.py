"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.

e.g.
   20
   / \
  10  30
     /  \
    25   35

i = BSTIterator(root)
i.next() = 10
i.next() = 20
i.next() = 25
...

"""
# Definition for a binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushleft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.pushleft(top.right)
        return top.val

    def pushleft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())