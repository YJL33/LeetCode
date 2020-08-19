"""
see https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""

import collections

class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        # helper
        # pass an alphabet counter while updating the result
        def dfs(node, seen=set()):
            cnt = [0 for _ in xrange(26)]   # a-z counter
            lbl = labels[node]
            if node not in seen:            # undirected graph, keep the visit history
                seen.add(node)
                for c in nd[node]:
                    sub = dfs(c, seen)
                    for i in xrange(26):    # update the counter
                        cnt[i] += sub[i]

                cnt[ord(lbl)-ord('a')] += 1     # add itself after done tracing all childrens
                res[node] = cnt[ord(lbl)-ord('a')]
            return cnt

        res = [0 for _ in xrange(n)]
        nd = collections.defaultdict(list)      # nodeDict
        for a, b in edges:
            nd[a] += b,
            nd[b] += a,
        dfs(0)
        return res


# print Solution().countSubTrees(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd")
# print Solution().countSubTrees(4, [[0,1],[1,2],[0,3]], "bbbb")
# print Solution().countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab")
# print Solution().countSubTrees(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa")
# print Solution().countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa")
ans = Solution().countSubTrees(4, [[0,2],[0,3],[1,2]], "aeed")
print(ans, ans == [1,1,2,1])

ans2 = Solution().countSubTrees(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],"abaedcd")
print(ans2, ans2 == [2,1,1,1,1,1,1])


