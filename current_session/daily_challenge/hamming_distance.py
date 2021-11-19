# simply go through all bits
# e.g. [10,4]
# 10: 0 1 0 1 0 => 1 0 1 => 1 0 => 1
# 4:  0 0 1 0 0 => 0 1 0 => 0 1 => 0
# hamming dist = 3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y: return 0
        cnt = 0
        while (x != 0 or y != 0):
            if (x%2 != y%2): cnt += 1
            x = x >> 1
            y = y >> 1
        return cnt