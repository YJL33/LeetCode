"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointers: 51ms
        # T: O(n)
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

    def twoSum(self, numbers, target):
        # dictionary: 68ms
        # T: O(n)
        dct = {}
        for i in xrange(len(numbers)):
            x = numbers[i]
            if target-x in dct:
                return [dct[target-x]+1, i+1]
            dct[x] = i

    def twoSum(self, numbers, target):
        # binary search: 116ms
        # for each number in numbers, seek for its counterpart.
        # T: O(n*logn)
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            temp_target = target - numbers[i]
            while l <= r:
                mid = l + (r-l)/2
                if numbers[mid] == temp_target:
                    return [i+1, mid+1]
                elif numbers[mid] > temp_target:
                    r = mid-1
                else:
                    l = mid+1
