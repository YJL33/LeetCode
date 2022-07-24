class Solution:
    def twoEggDrop(self, n: int) -> int:
        # divide the n into x spans, each span is having varied floors (y1-yx)
        # try span from low level, and once it breaks (at Xi), try floors from (Xi-1) to Xi
        # since it will save some tries at low floor, so we make early spans bigger than later ones
        # at most: we try x steps
        # e.g. 100: 
        # x = [9,22,34,45,55,64,72,79,85,90,94,97,99,100]   (try 1st at 9F, then 22F ... so on and so forth)
        # y = [9,12,11,10,9,8,7,6,5,4,3,2,1]
        if n <= 1: return 1
        if n == 2: return 2
        f, x = 1, n
        first_try = []
        while x > 0:
            first_try.append(x)
            x, f = x-f, f+1
        return len(first_try)