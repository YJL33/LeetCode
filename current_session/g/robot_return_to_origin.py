import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # check the overall movement
        cnt = {"L":0,"R":0,"D":0,"U":0}
        for m in moves:
            cnt[m] += 1
        return cnt["U"] == cnt["D"] and cnt["L"] == cnt["R"]
