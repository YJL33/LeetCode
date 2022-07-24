from typing import List
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # use bitwise operation
        # xor: we want to find two numbers have the highest bits complementing each other (0 and 1)
        # leverage xor property - if a^b=c, then we have a^c=b, b^c=a
        # check bit by bit until all bits are checked (we run exactly 32 times)
        # use mask to filter unwanted bits
        # e.g. given [3,10,5,25,2,8]
        # check from the highest bit (mask = [10000000])
        # 1st pass: mask=64  (10000000), numbers_after_masked: {0,64}           => ans=64
        # 2nd pass: mask=96  (11000000), numbers_after_masked: {0,32,64}        => ans=96
        # 3nd pass: mask=112 (11100000), numbers_after_masked: {0,64,32,80,48}  => ans=112
        # ... so on and so forth
        # time complexity: O(32n)
        if len(nums) < 2: return 0
        if len(nums) == 2: return nums[0]^nums[1]
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            masked_nums = set([num & mask for num in nums])
            # print('masked_nums:', masked_nums)
            # possible_max = ideal ans if exist two numbers complementing each other at this bit
            possible_max = ans | 1<<i
            for a in masked_nums:
                if possible_max^a in masked_nums:
                    ans = possible_max
                    break
            # print('ans:', ans, bin(ans))
        return ans

print(Solution().findMaximumXOR([3,10,5,25,2,8]))
print(Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))