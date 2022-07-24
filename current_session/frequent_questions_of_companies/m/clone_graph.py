
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# create new nodes first, and create a map: old->new
# for each new node, check its neighbors (by it's corresponding old node)
# and hook them by using map earlier created
import collections
class Solution:
    def cloneGraph(self, node:'Node') -> 'Node':

        nodeDict = collections.defaultdict(Node)        # key: old node, val: new node

        def deepCopy(node):
            if not node: return
            # copy its value
            newNode = Node(node.val)
            nodeDict[node] = newNode

            # hook/copy its neighbors
            for nb in node.neighbors:
                if nb in nodeDict:
                    newNode.neighbors.append(nodeDict[nb])
                else:
                    newNode.neighbors.append(deepCopy(nb))

            return newNode

        return deepCopy(node)
