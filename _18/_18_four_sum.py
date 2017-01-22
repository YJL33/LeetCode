"""
18. 4Sum

Given an array S of n integers,
are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

A solution set is: (-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def threeSum(nums, target, first):
            """
            3 sum problem
            """
            if len(nums) < 3: return []
            else:
                res = []
                nums.sort()         # Sort the array, O(nlogn)
                max_element = nums[-1]
                for j in xrange(len(nums)-2):
                    if j > 0 and nums[j] == nums[j-1]:      # next distinct nums[j]
                        continue
                    if nums[j]+2*max_element < target:      # nums[j] is too small
                        continue
                    if 3*nums[j] > target:                  # nums[j] is too large
                        continue
                    l, r = j+1, len(nums)-1     # l, r = smallest/biggest one in remaining elements
                    while l < r:
                        s = nums[j] + nums[l] + nums[r]     # sum of three elements
                        if s < target:                      # need bigger element
                            l +=1 
                        elif s > target:                    # need smaller element
                            r -= 1
                        else:
                            res.append([first, nums[j], nums[l], nums[r]])      # A unique quadlet
                            while l < r and nums[l] == nums[l+1]:               # move l to r
                                l += 1
                            while l < r and nums[r] == nums[r-1]:               # move r to l
                                r -= 1
                            l += 1; r -= 1              # next distinct l, r
                return res
        # below is main part
        if len(nums) < 4: return []
        else:
            ans = []
            length_of_nums = len(nums)
            nums.sort()         # Sort the array, O(nlogn)
            max_element = nums[-1]
            if 4*nums[0] > target or 4*max_element < target: return []  # Exist NO solution

            for i in xrange(len(nums)-3):
                if i > 0 and nums[i] == nums[i-1]:      # next distinct nums[i]
                    continue
                if nums[i]+3*max_element < target:      # nums[i] is too small
                    continue
                if 4*nums[i] > target:                  # nums[i] is too large
                    continue
                if 4*nums[i] == target and i+3 < length_of_nums and nums[i+3] == nums[i]:
                    ans.append([nums[i]]*4)             # Here's an unique solution
                    continue

                # Here has a valid nums[i] => Now solve 3 sum problem.
                temp_ans = threeSum(nums[i+1:], target-nums[i], nums[i])
                for q in temp_ans: ans.append(q)

        return ans