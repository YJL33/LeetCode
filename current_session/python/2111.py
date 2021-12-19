from typing import List
import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        # given K, parse arr into K sub arrays
        # need to check len(arr)-K spots
        # find LIS (Longest Increasing Sequence) in each subarray and add L-len(LIS)

        cnt = 0

        def count(A):
            lis = []
            for num in A:
                index = bisect.bisect_right(lis, num)
                if index == len(lis):
                    lis.append(num)
                else:
                    lis[index] = num
            return len(A) - len(lis)

        for x in range(k):
            cnt += count([arr[i] for i in range(x, len(arr), k)])
        
        return cnt

print(Solution().kIncreasing([5,4,3,2,1],1))
print(Solution().kIncreasing([4,1,5,2,6,2],2))
print(Solution().kIncreasing([4,1,5,2,6,2],3))
print(Solution().kIncreasing([1,2,3,4,5,6,7,8,9,10],2))
print(Solution().kIncreasing([1,9,3,8,5,7,7,6,9,5],2))
print(Solution().kIncreasing([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3],1), 'should be 12')
print(Solution().kIncreasing([3,9,4,1,3,1,3,9,5],1), 'should be 5')