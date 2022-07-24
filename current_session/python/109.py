# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    # restrictions on heights?
    # input validity? (e.g. null head)
    # upper/lowerbound of node.val?
    
    # use tortoise-hare algorithm to find mid, use as root tree node
    # and then recursively craft left and right tree nodes
    # tc: O(n*logn), avg tree height = logn, and scan through whole n in each level
    # sc: O(1)
    
    # idea:
    # use an array to store linked-list nodes, and then use binary-search-like to craft all tree nodes
    # tc: O(n) to scan linked-list and build array, O(n) to craft all tree nodes
    # sc: O(n) to store all nodes in array, O(h) to store ranges in stack, O(n) of output tree
    def sortedListToBST_arr(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head: return
        
        arr = []
        i, cur = 0, head
        while cur:
            arr.append(cur.val)
            cur, i = cur.next, i+1
        l, r, root = 0, i-1, TreeNode(0)
        st = [(l,r,root)]
        
        while st:
            ll, rr, node = st.pop()
            mm = (ll+rr)//2
            # node.val = node_dict[mm]
            node.val = arr[mm]
            if ll <= mm-1:
                node.left = TreeNode(0)
                st.append((ll, mm-1, node.left))
            if rr >= mm+1:
                node.right = TreeNode(0)
                st.append((mm+1, rr, node.right))
        
        return root
    
    
    # idea: (in-order-traversal)
    # in binary search tree, if we do in-order traversal, then we can get a sorted list (do opposite for this question)
    #
    # 0. make a global variable pointing at head
    # 1. find out the length of linked list first
    # 2. use recursive call to build the bst. the helper should: 
    #   a. build a sub-bst and return the root of sub-bst => need a range for recursive call, so that it'll know what to build
    #
    #   but how do we know the value of root??
    #      use global variable, after each recursive call, it should point at the end of the range.
    #      In other word, all ListNodes before pointer have been used in BST.
    #      now we can simply use the value of pointed ListNode as the value of the root of TreeNode.
    #   proof:
    #      consider we're using x-th ListNode as mid point (root)
    #      since the helper function is called x-1 times to craft all TreeNodes in the left sub-bst,
    #      the global variable pointer also moved x-1 times.
    #      which is exactly the pointing at the x-th ListNode that we want to use as mid TreeNode.
    #
    #   therefore the recursive call should also:
    #   b. move global variable (pointer) to the next after crafting root node
    #      
    # tc: O(n) to find the length of linked list, O(n) to craft all tree nodes
    # sc: O(h), where h is the height of recursive stack, O(n) of output tree
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return
        self.cur, L = head, 0
        while head:
            head, L = head.next, L+1

        def helper(l, r):
            if l > r: return None           # termination
            mid = (l+r)//2
            left = helper(l, mid-1)
            root = TreeNode(self.cur.val)
            self.cur = self.cur.next        # move it
            root.left = left
            root.right = helper(mid+1, r)
            return root
        
        return helper(0, L-1)
