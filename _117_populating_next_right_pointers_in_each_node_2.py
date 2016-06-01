"""
117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # if the node is someone's left => node.next should be someone's right, if exist.
        # if the node is someone's right => node.next should be someone.next.left, if exist.
        if root == None:
            return
        # move through layer by layer
        while root:      # something is here
            pointer = root          # point at here => beginning of this layer
            previous_branch = None
            while root:
                if previous_branch:
                    if root.left is not None:                   # assign previous branch
                        previous_branch.next = root.left
                    if root.left is None and root.right is not None:
                        previous_branch.next = root.right
                if root.left is not None and root.right is not None:    # something in bottom layer
                    root.left.next = root.right                         # assign left tree
                    previous_branch = root.right                        # temperiory store right tree
                if root.left is not None and root.right is None:        # Right branch is None
                    previous_branch = root.left
                if root.right is not None and root.left is None:
                    previous_branch = root.right
                root = root.next    # propogate toward right
            root = self.goNextLayer(pointer)
        return
    def goNextLayer(self, node):
        """
        go to next layer
        """
        if node.left is None and node.right is None and node.next is None:
            return
        if node.left is not None:
            return node.left
        if node.left is None and node.right is not None:
            return node.right
        if node.left is None and node.right is None:
            return self.goNextLayer(node.next)

