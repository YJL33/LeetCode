"""
116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    You may assume that it is a perfect binary tree
    (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
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
        # if the node is someone's left => node.next should be someone's right.
        # if the node is someone's right => node.next should be someone.next.left
        if root == None:
            return
        # move through layer by layer
        while root:      # something is here
            pointer = root          # point at here => beginning of this layer
            previous_right_tree = None
            while root:
                if previous_right_tree:
                    previous_right_tree.next = root.left                    # assign previous right tree
                if root.left is not None and root.right is not None:        # something in bottom layer
                    root.left.next = root.right                             # assign left tree
                    previous_right_tree = root.right                        # temperiory store right tree
                root = root.next    # propogate toward right
            root = pointer.left     # go next layer
        return




            


            