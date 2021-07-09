# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        def isMatch(s, t):
            if (s is None and t is not None) or (s is not None and t is None):
                return False
            elif s is None and t is None:
                return True

            if s.val == t.val:
                if isMatch(s.left, t.left) and isMatch(s.right, t.right):
                    return True
                else:
                    return False
        
        if isMatch(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)