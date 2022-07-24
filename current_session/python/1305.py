# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # iteratively collect all values
        # in-order traversal
        # tc: O(n)
        # sc: O(h), where h is the depth of stack, worst cast O(n)
        res = []
        st1, st2, cur1, cur2 = [], [], root1, root2
        while (st1 or cur1) and (st2 or cur2):
            while cur1:
                st1.append(cur1)
                cur1 = cur1.left
            while cur2:
                st2.append(cur2)
                cur2 = cur2.left
            
            cur1, cur2 = st1.pop(), st2.pop()       # get the smallest element from both
            if cur1.val <= cur2.val:                # add smaller element to result
                res.append(cur1.val)
                st2.append(cur2)
                cur1, cur2 = cur1.right, None
            else:
                res.append(cur2.val)
                st1.append(cur1)
                cur1, cur2 = None, cur2.right

        def clean(st, cur):
            nonlocal res
            while st or cur:
                while cur:
                    st.append(cur)
                    cur = cur.left
                cur = st.pop()
                res.append(cur.val)
                cur = cur.right
            return

        clean(st1, cur1)
        clean(st2, cur2)
        return res
            