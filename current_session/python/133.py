"""
133
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dfs and create deep copy
        if not node: return
        
        stack = [node]
        x = Node(node.val)
        cpDict = {node: x}
        visited = set()
        while stack:
            nd = stack.pop()
            visited.add(nd)
            xnb = []
            for n in nd.neighbors:
                if n not in cpDict:
                    cpDict[n] = Node(n.val)
                xnb += cpDict[n],
                if n not in visited:
                    stack += n,
            cpDict[nd].neighbors = xnb
        
        # print(x.neighbors)
        return x