from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        # only remove consecutively appeared characters
        # e.g. 
        # aaaaabbbbb => ab
        # aaaab => ab
        # 
        # first, get the consecutives
        toRmv = []      # list of consecutive characters
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            # print('i', i, 'j:', j)
            if (j-i) >= 2:
                toRmv.append((i,j))
            i = j
        # print('toRmv:', toRmv)
        res = 0
        for l, r in toRmv:
            res += sum(cost[l:r]) - max(cost[l:r])
        
        return res

print(Solution().minCost(s = "aaaaa", cost = [1,2,3,4,5]))
print(Solution().minCost(s = "abc", cost = [1,2,3]))
print(Solution().minCost(s = "aabaa", cost = [1,2,3,4,1]))
