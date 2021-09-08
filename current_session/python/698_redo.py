# naive approach
# eliminate edge cases (e.g. max(A) > avg(A))
# we can either:
# 1. prepare k buckets, try to distribute A[i] into each bucket
# 2. keep remove elements that sum == target
# e.g. sum(ai, aj, ak) == k, and return canPartitionKSubsets(A', k-3)

from typing import List
import bisect
class Solution:
    def canPartitionKSubsets(self, A: List[int], k: int) -> bool:
        # edge cases
        if k == 1: return True
        if k == len(A): return len(set(A))== 1

        # eliminate False cases
        A.sort()
        target = sum(A)//k
        if A[-1] > target or sum(A)%k != 0: return False

        # 
        while A[-1] == target:
            A.pop()
            k -= 1
        
        return self.helper(A, 0, target, k)
    
    def helper(self, arr, prevSum, tgt, k):
        if k == 0: return True
        J = bisect.bisect_left(arr, tgt-prevSum)
        if J < len(arr) and arr[J] == tgt-prevSum:
            self.helper(arr[:J] + arr[J+1:], 0, tgt, k-1)
        if J == len(arr) or arr[J] > tgt-prevSum: J -= 1

        for j in range(J, -1, -1):
            if prevSum+arr[j] == tgt:
                return self.helper(arr[:j] + arr[j+1:], 0, tgt, k-1)
            elif prevSum+arr[j] < tgt:
                if self.helper(arr[:j] + arr[j+1:], prevSum+arr[j], tgt, k):
                    return True
            else:
                break
        return False


print(Solution().canPartitionKSubsets([1,2,3,4], k = 3))
print(Solution().canPartitionKSubsets([4,3,2,3,5,2,1], k = 4))
print(Solution().canPartitionKSubsets([2,2,3,3,4], k = 2))
print(Solution().canPartitionKSubsets([1,1,1,1,1,1,1,2,2,3,3,4], k = 3))
print(Solution().canPartitionKSubsets([2,2,2,2,3,4,5],4))
print(Solution().canPartitionKSubsets([1,1,1,1,2,2,2,2],2))