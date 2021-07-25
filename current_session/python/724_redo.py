from typing import List

# count the sum of array
# from left to right, accumulate all elements
# if 2*leftSum == total: return i

class Solution():
    def pivotIndex(self, A: List[int]) -> int:
        total = sum(A)
        leftSum = 0
        for i in range(len(A)):
            if 2*leftSum == total-A[i]: return i
            leftSum += A[i]
        return -1