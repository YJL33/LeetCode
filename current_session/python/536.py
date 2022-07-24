# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    # clarification
    # type of node value?
    # restrictions on memory/timeout?
    # upperbound/lowerbound of node value?
    # number of nodes?
    # input validity?
    # binary tree, not binary search tree
    # balanced? could be very imbalanced?
    #
    # thoughts
    # looks like pre-order traversal 
    # (how to handle the parentheses?)
    # a. use recursive:
    # craft root, and then identify the range of left and right subtree with parentheses, give it into recursive function
    # termination criteria(?)
    # b. use iterative:
    # similarly, put the range into a stack
    #
    # dummy test case
    # 4(2(3)(1))(6(5))
    # root = 4, left tree 2(3)(1), right tree 6(5), so on and so forth
    #
    # ananlysis
    # recursive:
    # tc: O(nlogn), while using divide and conquer, we pass through leaves logn times, worst case O(n^2) for super imbalanced tree
    # sc: O(n) for output tree, O(d) where d is the depth of overhead recursive function calls, each includes some variables and parameters, worst case O(n)
    # iterative:
    # tc: O(nlogn), while using divide and conquer, we pass through leaves logn times, worst case O(n^2) for super imbalanced tree
    # sc: O(n) for output tree, O(d) where d is the avg size of stack, worst case O(n)
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        num = ''
        stack = []
        for i in s:
            if i.isdigit() or i == '-': 
                num += i
            elif i=='(': 
                if num: 
                    node = TreeNode(num)
                    num=''
                    stack.append(node)
            else:
                if num:
                    node = TreeNode(num)
                    num =''
                else: 
                    node = stack.pop()
                
                if stack[-1].left==None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

        return stack[-1] if stack else TreeNode(num) if s else None