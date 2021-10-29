from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # brute force
        # for all i j => calculate the value of v[i]+v[j]+i-j
        # time analysis: O(N^2)

        # keep update optimal v[i]+i
        # update the global maximum score
        # time analysis: O(N)

        optimalI = values[0]
        ans = float('-inf')
        for j in range(1, len(values)):
            localScore = values[j]-j + optimalI
            ans = max(localScore, ans)
            optimalI = max(values[j]+j, optimalI)       # update optimal I
        
        return ans

print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))
print(Solution().maxScoreSightseeingPair([1,2]))