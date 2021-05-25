"""
5429. The k Strongest Values in an Array

"""
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # sort
        # maintain 2 cursors, and get kth strongest value

        arr.sort()
        l, r = 0, len(arr)-1

        # if len(arr) %2:
        median = arr[(len(arr)-1)/2]
        # else:
        #     median = (arr[(len(arr)/2)-1] + arr[len(arr)/2])/2

        res = []

        while len(res) < k:
            # print arr[r], arr[l], median
            if abs(arr[r] - median) >= abs(arr[l]-median):
                res += arr[r],
                r -= 1
            else:
                res += arr[l],
                l += 1

        return res

print Solution().getStrongest([1,2,3,4,5], 2)
print Solution().getStrongest([1,1,3,5,5], 2)
print Solution().getStrongest([6,7,11,7,6,8], 5)
print Solution().getStrongest([6,-3,7,2,11], 3)
print Solution().getStrongest([-7,22,17,3], 2)
