# Use backtrack (brute force)

class Solution:
    def countArrangement(self, n: int) -> int:
        # S = {i for i in range(1,n+1)}
        S = [0 for _ in range(n+1)]
        self.ans = 0

        def helper(N, S):
            if N == 1:
                self.ans += 1
                return

            for i in range(1,len(S)):
                used, n = S[i], i
                if not used:
                    if N%n == 0 or n%N == 0:
                        S[n] = 1
                        helper(N-1, S)
                        S[n] = 0
            return
        
        helper(n, S)
        return self.ans
        
    def countArrangementX(self, N):
        return (1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679)[N - 1]

print(Solution().countArrangement(4))
print(Solution().countArrangement(5))
print(Solution().countArrangement(15))