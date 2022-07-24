from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt_dict = {0:-1}
        balance = 0
        max_dist = float('-inf')
        for i, n in enumerate(nums):
            if n == 1:
                balance += 1
            else:
                balance -= 1
            if balance in cnt_dict:
                max_dist = max(max_dist, i-cnt_dict[balance])
            else:
                cnt_dict[balance] = i
        return max_dist
