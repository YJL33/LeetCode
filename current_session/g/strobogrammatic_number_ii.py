from typing import List
class Solution:
    def findStrobogrammatic(self, n:int, zero=False)->List[str]:
        # observation: 0,1,8<->0,1,8, 6<->9
        if n == 1: return ["0","1","8"]
        if n == 2: return ["11","69","88","96"]
        
            

print(Solution().findStrobogrammatic(1))
print(Solution().findStrobogrammatic(2))
print(Solution().findStrobogrammatic(3))
print(Solution().findStrobogrammatic(4))