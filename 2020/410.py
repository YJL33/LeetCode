"""
410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 <= n <= 1000
1 <= m <= min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # use binary search
        # left = max(arr)
        # right = sum(arr)
        if (m == 1): return sum(nums)

        l, r = max(nums), sum(nums)
        lastLegit = None

        while l <= r:
            mid = (l + r)//2
            # print l, r, mid
            isValid = self.isValid(nums, m, mid)
            if isValid:     # the number could be too big
                lastLegit = mid
                r = mid - 1
            else:
                l = mid + 1

        return l

    def isValid(self, arr, m, n):
        # verify whether we can use the target number (n) as to split the array or not
        i, sumOfGroup = 0, 0
        res = []
        for i in xrange(len(arr)):
            sumOfGroup += arr[i]
            if sumOfGroup > n:
                res += sumOfGroup-arr[i],
                sumOfGroup = arr[i]

        res += sumOfGroup,

        return (m >= len(res))

print Solution().splitArray([7,2,5,10,8], 2)
print Solution().splitArray([7,2,5,10,8], 1)
print Solution().splitArray([7,2,5,10,8], 5)