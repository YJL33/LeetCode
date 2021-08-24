from typing import List
class Solution:
    def nextPermutation(self, A: List[int]) -> None:
        # algorithm:
        # find and Reverse
        # find j and k -> swap
        # j: largest j s.t. A[j] < A[j+1]
        # k: largest k s.t. A[j] < A[k]
        # reverse A[j+1:]

        # [1,2,3] -> [1,3,2]    j=1, k=2 ,swap 2 and 3, reverse A[2:]
        # [1,3,2] -> [2,1,3]    j=0, k=2 ,swap 1 and 2, reverse A[1:]
        # [2,1,3] -> [2,3,1]    j=1, k=2 ,swap 1 and 3, reverse A[2:]
        # [2,3,1] -> [3,1,2]    j=0, k=1 ,swap 2 and 3, reverse A[1:]

        if not A: return
        # print('be4or:', A)
        a, b = self.finder(A)
        if a == -1:
            A.reverse()
            return

        A[a], A[b] = A[b], A[a]
        # print('tmp:', A, 'a:', a, 'b:', b)
        l, r = a+1, len(A)-1
        while l < r:
            A[l], A[r] = A[r], A[l]
            l, r = l+1, r-1
        # print('after:', A)
        return

    def finder(self, A):
        i = len(A)-2
        while i >= 0:
            if A[i] < A[i+1]:
                break
            i -= 1

        if i == -1: return -1, -1
        
        j = len(A)-1
        while j >= 0:
            if A[j] > A[i]:
                break
            j -= 1
        # print("i, j", i, j)
        return i, j

print(Solution().nextPermutation([1,2,3]))
print(Solution().nextPermutation([1,3,2]))
print(Solution().nextPermutation([2,1,3]))
print(Solution().nextPermutation([2,3,1]))