"""
Also apply dictionary data structure
"""
class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        list = [element for element in dict if dict[element] == 1]
        return list