"""
402
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # observation: n=143, k=1: remove 4, which is the first n[i]>n[i+1]
        # handle corner case: 0
        if k == len(num): return 0
        
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            # print('stack:', ''.join(stack))

        # handle corner case: 1111
        while k:
            stack.pop()
            k -= 1
        
        return ''.join(stack).lstrip('0') or '0'

print(Solution().removeKdigits(num = "1432219", k = 3))
print(Solution().removeKdigits(num = "111111", k = 3))
print(Solution().removeKdigits(num = "10200", k = 1))
print(Solution().removeKdigits(num = "10", k = 2))