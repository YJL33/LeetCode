import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return collections.Counter(nums).most_common(1)[0][0]
        pick, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if cnt == 0:
                cnt, pick = cnt+1, nums[i]
            elif nums[i] == pick:
                cnt += 1
            else:
                cnt -= 1
        return pick