from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def bs():
            l, r = 0, len(arr)-1
            while l < r:
                m = l + (r-l)//2
                if arr[m-1]<arr[m] and arr[m]>arr[m+1]:
                    return m
                elif arr[m-1]<arr[m] and arr[m]<arr[m+1]:       # at the right side
                    l = m+1
                elif arr[m-1]>arr[m] and arr[m]>arr[m+1]:       # at the left side
                    r = m
                else:
                    print("?")
            return l

        pk = bs()
        return pk

print(Solution().peakIndexInMountainArray([0,1,0]))
print(Solution().peakIndexInMountainArray([0,2,1,0]))
print(Solution().peakIndexInMountainArray([0,10,5,2]))
print(Solution().peakIndexInMountainArray([3,4,5,1]))
print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
