"""
209
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        if not n: return False
        if n == 1: return True

        # direct implementation
        # 7 49 16+81=97 81+49=130 1+9=10 1

        def helper(x):
            s = 0
            while x:            # start from smallest digit
                x, s = x//10, s+pow(x%10, 2)
            return s
        
        res = helper(n)

        if res > 10:
            return self.isHappy(res)
        else:
            return res in [1,7,10]