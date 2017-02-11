"""
 16. 3Sum Closest

    Total Accepted: 112528
    Total Submissions: 367235
    Difficulty: Medium
    Contributors: Admin

Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return []
        nums.sort()
        res, last, diff = None, len(nums)-1, float('inf')
        for i, a in enumerate(nums):
            j, k = i+1, last
            while j < k:
                # print i, j, k, a, nums[j], nums[k]
                tmpsum = a + nums[j] + nums[k]

                if abs(tmpsum - target) < diff:
                    diff, res = abs(tmpsum - target), tmpsum

                if tmpsum > target: k -= 1
                else: j += 1

        return res

def main():
    print Solution().threeSumClosest([-1,55,12,33], 1)

if __name__ == '__main__':
    main()