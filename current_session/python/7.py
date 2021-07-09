class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return x
        isPositive = (x > 0)
        if not isPositive: x = -x
        res = 0
        while x:
            res= res*10 + x%10
            x = x//10
        if isPositive:
            return res if res<=(pow(2,31)-1) else 0
        else:
            return -1*res if (-1*pow(2,31))<=(-1*res) else 0
print(Solution().reverse(123))
print(Solution().reverse(1000000000))