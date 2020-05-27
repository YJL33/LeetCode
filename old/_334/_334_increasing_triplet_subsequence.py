"""
 334. Increasing Triplet Subsequence

    Total Accepted: 29205
    Total Submissions: 77964
    Difficulty: Medium
    Contributors: Admin

Given an unsorted array return whether an increasing subsequence of length 3 exists in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≦ i < j < k ≦ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 3: return False
        triplet, cand = [nums[0]], []                       # say A < B < C
        for n in nums[1:]:
            if n > triplet[-1]:
                triplet += n,
            elif len(triplet) == 1 and n < triplet[0]:
                triplet[0] = n                              # a better A
            elif len(triplet) == 2:
                if n > triplet[0] and n < triplet[1]:
                    triplet[1] = n                          # a better B
                elif n < triplet[0]:
                    if not cand:
                        cand += n,                          # already got A and B, now A'
                    elif n > cand[0]:
                        cand += n,                          # already got A, B and A', now B'
                        triplet, cand = cand, []            # replace A, B with A' and B'
                    elif n < cand[0]:
                        cand[0] = n                         # got a better A'
            if len(triplet) == 3: return True

        return False