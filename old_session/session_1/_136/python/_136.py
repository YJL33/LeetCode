"""
 136. Single Number

    Total Accepted: 191187
    Total Submissions: 360705
    Difficulty: Easy
    Contributors: Admin

Given an array of integers,
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for n in nums[1:]:
            ans ^= n
        return ans
        

def main():
    print Solution().singleNumber([3,4,5,6,7,8,9,8,7,6,5,4,3])

if __name__ == "__main__":
    main()