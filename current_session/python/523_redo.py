from typing import List

# use dictionary
# we go through the array, and keep adding elements s.t. lsum = sum(A[:i+1])
# key: lsum%k, value: i
# if key exist in dictionary: return true if j-i >= 2
# so on and so forth

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        lsum = 0
        nd = {0:-1}                 # consider subarray begin from 0
        for j in range(len(nums)):
            lsum = (lsum+nums[j])%k
            if lsum in nd:          # A[i+1:j] is the subarray
                if j-nd[lsum] >= 2: return True
            else:
                nd[lsum] = j
            # print("nd:", nd)
        return False

print(Solution().checkSubarraySum([23,2,4,6,7], 6))
print(Solution().checkSubarraySum([23,2,6,7,4], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], k = 13))
print(Solution().checkSubarraySum([1,2,3],5))

