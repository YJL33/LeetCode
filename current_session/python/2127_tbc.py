from typing import List
import collections
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # graph
        # 1. find the biggest circle
        # 2. find the sum of chain (that has a<->b included inside)
        n = len(favorite)
        def check_circle(i):
            visited, group, root = set(), [], i
            while i not in visited:
                visited.add(i)
                group.append(i)
                i = favorite[i]
            while favorite[group[-1]] != root:
                group.pop()
            return len(group)
        def get_biggest_circle():
            # start from each point and see if the tail has favorite == root
            max_seen = 0
            for i in range(n):
                max_seen = max(check_circle(i), max_seen)
            return max_seen
        
        def get_sum_of_chain():
            # craft adj list
            adj = collections.defaultdict(list)
            for i in range(n):
                adj[favorite[i]].append(i)
            # search all nodes
            for i in range(n):
                if i != favorite[i]: continue
                a, b = i, favorite[i]
                
            return 

        
        sum_of_chain = get_sum_of_chain()
        biggest_circle = get_biggest_circle()

        return max(sum_of_chain, biggest_circle)

print(Solution().maximumInvitations([2,2,1,2]))
print(Solution().maximumInvitations([1,2,0]))
print(Solution().maximumInvitations([3,0,1,4,1]), 'sb 4')
print(Solution().maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8]), 'sb 6')