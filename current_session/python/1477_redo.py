# use partial sum and dictionary
# find subarray has sum equal to target first
# and then pick the shortest non-overlapped Two (use heap(?))
# analysis: O(n) + O(m^2)

# similar method
# use partial sum and dictionary
# for each i, split the array into two parts and find subarray sum == target
# keep update the result
# analysis O(n) + O(n)

from typing import List
import collections
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pSum = [0]
        seenSum = collections.defaultdict(list)
        seenSum[0].append(-1)
        for i in range(len(arr)):
            a = arr[i]
            pSum.append(pSum[-1]+a)
            currentSum = pSum[-1]
            seenSum[currentSum].append(i)

        # print('pSum', pSum)               # e.g. [7,4,3,7] -> [0, 7, 11, 14, 21]
        res = float('inf')
        minL = float('inf')
        for i in range(1,len(pSum)):
            # left side
            if pSum[i]-target in seenSum:
                lstart, lend = seenSum[pSum[i]-target][0], i
                minL = min(minL, lend-lstart)
            # right side
            if pSum[i]+target in seenSum:
                rstart, rend = i, seenSum[pSum[i]+target][0]
                res = min(res, minL+rend-rstart)

        return res if res != float('inf') else -1

print(Solution().minSumOfLengths([3,2,2,4,3],3))
print(Solution().minSumOfLengths([7,4,3,7],7))
print(Solution().minSumOfLengths([4,3,2,6,2,3,4],6))
print(Solution().minSumOfLengths([5,5,4,4,5], 3))
print(Solution().minSumOfLengths([3,1,1,1,5,1,2,1], 3))
                