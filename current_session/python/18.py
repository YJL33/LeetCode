"""
https://leetcode.com/problems/4sum/
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # think about 3-sum
        # leverage negative and find find 2-sum
        if len(nums) < 4:
            return []
        else:
            res = {}
            nums.sort()
            for i in range(len(nums)):
                tmp = self.threeSum(nums[i+1:], target-nums[i])
                # print tmp
                if tmp != None:
                    for x in tmp:
                        x = (nums[i],x[0],x[1],x[2])
                        res[x] = 1
            return [[k[0], k[1], k[2], k[3]] for k in res.keys()]

    def threeSum(self, nums, t):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # print nums, t
        if len(nums) < 3: return []
        if len(nums) >= 3:
            res = []
            # nums.sort()         # Sort the array, O(nlogn)
            max_element = nums[-1]
            for i in xrange(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:  # next distinct i
                    continue
                if (nums[i]+2*max_element < t):     # i is too small
                    continue
                if (3*nums[i] > t):                 # i is too large
                    continue
                l, r = i+1, len(nums)-1     # l, r = smallest/biggest one in remaining elements
                while l < r:
                    s = nums[i] + nums[l] + nums[r]     # sum of three elements
                    if s < t:               # need bigger element
                        l +=1 
                    elif s > t:             # need smaller element
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])     # A unique triplet
                        while l < r and nums[l] == nums[l+1]:       # move l to r w/o changing value
                            l += 1
                        while l < r and nums[r] == nums[r-1]:       # move r to l w/o changing value
                            r -= 1
                        l += 1; r -= 1              # next distinct l, r
            return res

# print(Solution().fourSum([1,0,-1,0,-2,2], 0))
# print(Solution().fourSum([5,5,3,5,1,-5,1,-2],4))
print(Solution().fourSum([-1,-5,-5,-3,2,5,0,4],-7))