from typing import List
class Solution:
    def findMin(self, A: List[int]) -> int:
        # find pivot
        # exclude edge cases
        # if there's no rotate: A[0] must < A[-1]
        # if A[0] == A[-1] => keep tracking for the head and tail
        l, r = 0, len(A)-1

        while l < r:
            m = (l+r)//2
            if A[m] > A[r]:     # pivot at the right side
                l = m+1
            elif A[m] < A[r]:   # pivot at the left side
                r = m
            else:
                r -= 1

        return A[l]

# print(Solution().findMin([1,3,5]), 'should be 1')
# print(Solution().findMin([2,2,2,0,1]), 'should be 0')
# print(Solution().findMin([2,2,2]), 'should be 2')
# print(Solution().findMin([0,1,3,4,5,6,7]), 'should be 0')
# print(Solution().findMin([5,6,7,0,2,3,4]), 'should be 0')
# print(Solution().findMin([4,6,7,0,2,3,4]), 'should be 0')
# print(Solution().findMin([2,2,2,2,2,2,2]), 'should be 2')
print(Solution().findMin([1,2,1]), 'should be 1')
