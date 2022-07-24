from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []
        candidates.sort()
        
        def dfs(start, target, path):
            if target == 0:
                self.res.append(path)
                return
            for i in range(start, len(candidates)):
                a = candidates[i]
                if i > start and a == candidates[i-1]:      # important to avoid duplicate
                    continue
                if a > target:                              # no need to find anymore
                    break
                dfs(i+1, target-a, path+[a])
            return
        
        dfs(0, target, [])
        
        return self.res
