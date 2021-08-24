# diameter of binary tree
# diameter is the length of longest path b/w any 2 nodes in a tree
# may or may not pass root

# for each node, find out the longest path of its both children
# update the global solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        self.diameter = 0
        
        def getMaxPath(node):
            if not node: return 0
            l = getMaxPath(node.left) if node.left else 0
            r = getMaxPath(node.right) if node.right else 0
            self.diameter = max(self.diameter, l+r)
            return max(l, r)+1
        
        getMaxPath(root)
        return self.diameter

e = TreeNode(5)
d = TreeNode(4)
c = TreeNode(3)
b = TreeNode(2, d, e)
a = TreeNode(1, b, c)
print(Solution().diameterOfBinaryTree(a))