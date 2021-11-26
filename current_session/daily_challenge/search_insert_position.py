class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # implement bisect_left
        def bs_left(arr, x):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] < x:       # too small, search right side
                    l = m+1
                else:                   # too big / equal to x, search better x
                    r = m
            return l
        
        return bs_left(nums, target)

print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))