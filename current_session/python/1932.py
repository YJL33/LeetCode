# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
import collections
class Solution:
    # clarification
    # are all roots unique?
    # upperbound/lowerbound of node.val
    # 
    # first, collect tree info
    # each unique node value can only appear at most 2 trees, (if more, return False)
    # if all node values in a tree has never appeared on other trees, return False
    # To craft the merged bst, start from the root that never appeared in other tree (level-order traversal)
    # if we have more than one? return False
    #
    # merging can not happen as root-root, since there's no common node at root
    # merging can not happen "at the same side", e.g. [5,1,6],[3,2,6], 6 is common node but at the same side
    # merging can not hapepn as "leaf-leaf", another case [2,1,3],[4,3,5]
    # so the merging must happen on: leaf-root
    #
    # to check the validity, we can sort the root value
    # say we have r, all nodes in the left side of r should not have value more than r
    # e.g. [[5,3,8],[3,1,1000]], after sort -> [3,1,10000], [5,3,8] => 10000 >= 5 => invalid
    #
    # algorithm:
    # visit all nodes to collect the occurance info
    # sort all roots (do we need to sort? or we can check while crafting?)
    # start to craft the merged tree, (level-order traversal):
    # 1. start from root that never appeared
    # 2. check both leaves, pick the overlapped and merge it
    # 3. while crafting, pass the upperbound/lowerbound as checker
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:

        self.is_valid = True
        
        def _update_tree(node, idx=0):      # idx: root = 0, leaf = 1
            if not node: return
            nonlocal tdict
            if node.val in tdict:
                if tdict[node.val][idx] is not None:
                    self.is_valid = False
            else:
                tdict[node.val] = [None, None]
            tdict[node.val][idx] = node
            _update_tree(node.left, 1)
            _update_tree(node.right, 1)
            return
        
        # collect tree info
        # tdict: dictionary, key: node.val, value: [node as root, node as leave]
        tdict = collections.defaultdict(list)
        for t in trees:
            _update_tree(t)
            if not self.is_valid: return
        
        # print('tree_info',[(k, v[0].val if v[0] else 0, v[1].val if v[1] else 0) for k, v in tdict.items()])

        # find the root to begin with
        root = None
        for k, v in tdict.items():
            if not v[1]:
                if root: self.is_valid = False
                root = v[0]
            if not self.is_valid: return
        
        if not root: return
        # print('root', root.val)

        # craft the merged bst
        tree_cnt = 0
        dq = collections.deque()
        dq.append((root, None, float('-inf'), float('inf'), 1))
        while dq and self.is_valid:
            node, parent, lowerbound, upperbound, add = dq.popleft()
            tree_cnt += add
            # print('current:',node.val, parent.val if parent else None, lowerbound, upperbound )
            if parent:
                if lowerbound < node.val < upperbound:
                    if node.val < parent.val:
                        parent.left = node
                    else:
                        parent.right = node
                else:
                    self.is_valid = False
            if node.left:
                left_child = tdict[node.left.val][0] if tdict[node.left.val][0] is not None else node.left
                dq.append((left_child, node, lowerbound, min(upperbound, node.val), left_child != node.left))
            if node.right:
                right_child = tdict[node.right.val][0] if tdict[node.right.val][0] is not None else node.right
                dq.append((right_child, node, max(lowerbound, node.val), upperbound, right_child != node.right))
        # print('cnt', tree_cnt)
        return root if self.is_valid and tree_cnt == len(trees) else None