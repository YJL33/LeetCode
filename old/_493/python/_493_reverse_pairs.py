"""
493. Reverse Pairs

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Hard

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

    The length of the given array will not exceed 50,000.
    All the numbers in the input array are in the range of 32-bit integer.
"""
class Solution(object):
    def __init__(self):
        self.cnt = 0
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def msort(lst):
            # merge sort body
            L = len(lst)
            if L <= 1:                          # base case
                return lst
            else:                               # recursive case
                return merger(msort(lst[:int(L/2)]), msort(lst[int(L/2):]))
        def merger(left, right):
            # merger
            l, r = 0, 0                         # increase l and r iteratively
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    self.cnt += len(left)-l     # add here
                    r += 1
            return sorted(left+right)

        msort(nums)
        return self.cnt


def main():
    test = [1,1,-1,-1,-1,1]
    test2 = [5,4,3,2,1]
    test3 = [9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
    test4 = [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
    print Solution().reversePairs(test), " <=  should be 9"
    print Solution().reversePairs(test2), " <=  should be 4"
    print Solution().reversePairs(test3), " <=  should be 69"
    print Solution().reversePairs(test4), " <=  should be 9"

if __name__ == '__main__':
    main()
