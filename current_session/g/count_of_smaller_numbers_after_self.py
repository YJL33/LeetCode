from typing import List
class Solution:
    def countSmaller(self, nums:List[int]) -> List[int]:

        self.counter = [0 for _ in range(len(nums))]

        # merge sort: O(nlogn)
        def msort(A):
            if len(A) <= 1: return A
            m = len(A)//2
            l, r = msort(A[:m]), msort(A[m:])
            i, j = 0, 0
            ans = []
            cross = 0
            while i < len(l) and j < len(r):
                if l[i][0] <= r[j][0]:
                    ans.append(l[i])
                    self.counter[l[i][1]] += cross
                    i += 1
                else:
                    cross += 1
                    ans.append(r[j])
                    j += 1
            while i < len(l):
                ans.append(l[i])
                self.counter[l[i][1]] += cross
                i += 1
            while j < len(r):
                ans.append(r[j])
                j += 1
            return ans

        A = []
        for i in range(len(nums)):
            A.append((nums[i], i))
        # print("before:", A)
        
        A = msort(A)
        # print("after :", A)
        return self.counter

print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmaller([4,3,2,1]))
print(Solution().countSmaller([-1]))
