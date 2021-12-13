from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # use monotonic (decreasing) stack
        ms = []
        ans = 0
        prevGap = 0
        for i in range(len(nums)):
            n = nums[i]
            if not ms or n < nums[ms[-1]]:
                for x in ms:
                    ans += nums[x]-n
                ms += i,
                if prevGap: ans += prevGap
            else:
                # pop n and add the range to it
                minVal = nums[ms[-1]]
                tmp = 0
                while ms and n >= nums[ms[-1]]:
                    tmp += n-minVal
                    ms.pop()
                ans += tmp
                ms += i,
                prevGap = tmp
            print('i', i, 'ans', ans)
        
        print('ms', [nums[i] for i in ms])
        
        return ans

print(Solution().subArrayRanges([4,-2,-3,4,1]))
print(Solution().subArrayRanges([1,2,3]))
print(Solution().subArrayRanges([1,3,3]))