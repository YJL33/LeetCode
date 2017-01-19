"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 1st way: read the linked-list as an array, then call #108. (beats 8%)
        # 2nd way: use "fast-slow" pointer to find the mid-point.    (beats 60%)
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # after the above loop, "slow.next" would be mid-point (root)
        # cut the original listnode here, and seek for root's children from both part.
        temp = slow.next
        slow.next = None
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root

