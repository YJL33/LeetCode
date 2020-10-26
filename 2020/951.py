"""
see https://leetcode.com/problems/flip-equivalent-binary-trees/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # use 2 pointers and all nodes while visiting all nodes

        if not root1 and not root2: return True

        dq = deque([(root1, root2)])

        while dq:
            p1, p2 = dq.popleft()

            # compare p1 and p2
            # if same => add their children into dq by order

            if (p1 and p2) and (p1.val == p2.val):
                # compare both children and add them into dq
                p1children, p2children = [], []
                if p1.left: p1children += (p1.left.val, p1.left),
                if p1.right: p1children += (p1.right.val, p1.right),
                if p2.left: p2children += (p2.left.val, p2.left),
                if p2.right: p2children += (p2.right.val, p2.right),
                
                if len(p1children) != len(p2children):
                    return False
                else:
                    p1children.sort()
                    p2children.sort()
                    i = 0
                    while i < len(p1children):
                        dq.append((p1children[i][1], p2children[i][1]))
                        i += 1

            else:
                return False

        return True