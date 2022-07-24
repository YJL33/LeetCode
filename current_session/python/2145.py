from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # use prefix-sum
        prefix = [0]
        for d in differences:
            prefix.append(prefix[-1]+d)
        if max(prefix)-min(prefix) > upper-lower: return 0
        return (upper-lower) - (max(prefix)-min(prefix)) + 1