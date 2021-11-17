class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # simply re-arrange down and right, and see how many permutations there
        return int(self.factorial(m+n-2)/(self.factorial(m-1)*self.factorial(n-1)))
    
    def factorial(self, x):
        ans = 1
        while x > 0:
            ans, x = ans*x, x-1
        return ans

print(Solution().uniquePaths(3,7))
print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(7,3))
print(Solution().uniquePaths(3,3))