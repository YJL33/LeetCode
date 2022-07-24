# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # clarification
        # dummy cases are not allowed (what if allowed?)
        # validity of input (will target always exist?)
        # 
        # thoguhts / algorithm
        # with target node, we can simply search the cloned node, with pre-order traversal
        # with repeat, we should use 2 cursors (also pre-order traversal but visit both tree)
        # 
        # dummy test cases
        # edge cases
        # (empty tree?)
        #
        # analysis:
        # tc: O(d) where d is the depth of target, worst case O(N)
        # sc: O(1) for 2 cursors, O(d) for recursive call stack, worst case O(N)
        cur1, cur2 = original, cloned
        self.target_ref = None
        # pre-order traverse both tree to find the target node
        def finder(original_cursor, cloned_cursor):
            if self.target_ref:
                return
            if original_cursor == target:
                self.target_ref = cloned_cursor
                return
            if original_cursor.left:
                finder(original_cursor.left, cloned_cursor.left)
            if original_cursor.right:
                finder(original_cursor.right, cloned_cursor.right)
            return
        
        finder(cur1, cur2)
        return self.target_ref
            
            