# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node:'Node') -> 'Node':

        def copyNode(node, visited={}):
            if not node: return
            newNode = Node(node.val)
            visited[node] = newNode
            if node.neighbors:
                for n in node.neighbors:
                    if n not in visited:
                        newNode.neighbors.append(copyNode(n, visited))
                    else:
                        newNode.neighbors.append(visited[n])
            return newNode

        return copyNode(node)
        