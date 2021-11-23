from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1: return [[x] for x in range(1, n+1)]
        ans = []
        st = []
        for i in range(1,n+1):
            tmp = []
            if st:
                for s in st:
                    if len(s) == k-1: ans.append(s+[i])
                    else: tmp.append(s+[i])
            st += tmp
            st.append([i])
        return ans

print(Solution().combine(4,2))
print(Solution().combine(1,1))
