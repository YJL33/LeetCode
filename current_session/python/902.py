from typing import List
import bisect
class Solution:
    def atMostNGivenDigitSet_TLE(self, digits: List[str], n: int) -> int:

        # generate the candidates and use bisect to find the numbers
        # TLE: wasted too much time on generating digits have length < n
        cands = [int(x) for x in digits]
        d = [int(x) for x in digits]
        # e.g [1,2,3,5,7], given 3
        if n <= 10: return bisect.bisect_right(cands, n)

        cnt = 0
        while n > cands[-1]:
            cnt += len(cands)
            cands = [10*t + k for t in cands for k in d]
        
        cnt += bisect.bisect_right(cands, n)
        return cnt

    def atMostNGivenDigitSet_ans(self, D, N):
        N = str(N)
        n = len(N)
        # add all generated numbers that has length < n
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        # add digit by digit (from left to right?)
        # check the digit of given N and calculate the possible outcomes
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)

print(Solution().atMostNGivenDigitSet(["1","2","3","4","6","7","8","9"],67688637))
print(Solution().atMostNGivenDigitSet(["1","2","3","4","5","6","7","8","9"],74546987))
