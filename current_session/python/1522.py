"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # for each node, the length of diameter is:
        # max(diameter of left, diameter of right, 2+diameter pass left+diameter pass right)

        # d: diameter of node, c: longest path that start from (or end with) node
        def helper(node):
            if not node.children: return (0, 0)
            cs, ds = [], []
            for child in node.children:
                cd, cc = helper(child)
                ds.append(cd)
                cs.append(cc)
            cs.sort()
            if len(cs) >= 2:
                ds.append(2+cs[~0]+cs[~1])
            d = max(ds)
            c = 1+cs[-1]
            # print('node:', node.val, d, c)
            return (d, c)
        
        a, b = helper(root)
        return max(a, b)