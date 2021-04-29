"""
1344
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        L = minutes*6       # long pointer
        S = (hour%12 + (minutes/60.0))*30# short pointer

        diff = abs(L-S)

        return min(diff, 360-diff)