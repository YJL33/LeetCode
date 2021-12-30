# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

from typing import List
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seenNode = set()
        seenChildren = set()
        for n in tree:
            for c in n.children:
                seenChildren.add(c)
                if c in seenNode:
                    seenNode.remove(c)
            if n not in seenChildren:
                seenNode.add(n)
        
        assert(len(seenNode) == 1)
        return list(seenNode)[0]
