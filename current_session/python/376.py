from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = [nums[0]]
        diff = None
        for i in range(1,len(nums)):
            n, prev = nums[i], res[-1]
            if n == prev:
                continue
            if not diff or (n-prev)*diff < 0:
                res.append(n)
                diff = -1 if (n-prev < 0) else 1
            else:
                res.pop()
                res.append(n)
        # print('res:', res)
        return len(res)

print(Solution().wiggleMaxLength([1,7,4,9,2,5]))
print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(Solution().wiggleMaxLength([1,1,1,1,1,1,1,1,1,1]))
print(Solution().wiggleMaxLength([2]))
print(Solution().wiggleMaxLength([1,2,1,2,1,2,1,2,3,4,5,6,7,8,9,8,9,8,9,8,9,8,9,8,9,8,9,8,9,8]))
