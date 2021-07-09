"""
see https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)%k != 0:
            return False

        numOfArrays = len(nums)//k

        nd = {}
        for n in nums:
            if n in nd:
                nd[n] += 1
            else:
                nd[n] = 1

        keys = nd.keys()
        keys.sort()
        i = 0

        # construct the subarray, pick-up from the smallest element
        while numOfArrays > 0:
            while nd[keys[i]] == 0:
                i += 1
            a, toAdd = keys[i], k
            while toAdd:
                if a not in nd or nd[a] == 0:
                    return False
                nd[a] -= 1
                toAdd -= 1
                a += 1
            numOfArrays -= 1

        return True

print(Solution().isPossibleDivide([1,2,3,4], 3))
print(Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3))
print(Solution().isPossibleDivide([3,3,2,2,1,1], 3))
print(Solution().isPossibleDivide([1,2,3,3,4,4,5,6], 4))
print(Solution().isPossibleDivide([1,2,3,3,4,4,5,6,8,9,10,11,1,2,3,4,2,3,4,5,3,4,5,6],4))
print(Solution().isPossibleDivide([2,4,6,8],4))
print(Solution().isPossibleDivide([1,2,3,4,6],4))
