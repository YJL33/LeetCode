"""
844
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.helper(S) == self.helper(T)
    
    def helper(self, A):
        i, stack = 0, []
        while i < len(A):
            if A[i] != "#":
                stack += A[i],
            elif stack:
                stack.pop()
            i += 1
        return "".join(stack)
    
    def backspaceCompare2(self, S: str, T: str) -> bool:
        a, b = self.helper2(S, len(S)-1), self.helper2(T, len(T)-1)
        while S[a] == T[b] and a >= 0 and b >= 0:
            a, b = self.helper2(S, a-1), self.helper2(T, b-1)
        return a == b == -1
    
    def helper2(self, A, i):
        cnt = 0
        while i >= 0:
            if A[i] == "#":
                cnt += 1
                i -= 1
            elif cnt > 0:
                cnt -= 1
                i -= 1
            else:
                return i
        return -1



# print(Solution().backspaceCompare("ab#c","ad#c"))
# print(Solution().backspaceCompare("ab##","c#d#"))
# print(Solution().backspaceCompare("a##c","#a#c"))
# print(Solution().backspaceCompare("a#c","b"))
# print(Solution().backspaceCompare("nzp#o#g","b#nzp#o#g"))



# print(Solution().backspaceCompare2("ab#c","ad#c"))
# print(Solution().backspaceCompare2("ab##","c#d#"))
# print(Solution().backspaceCompare2("a##c","#a#c"))
# print(Solution().backspaceCompare2("a#c","b"))
print(Solution().backspaceCompare2("nzp#o#g","b#nzp#o#g"))
print(Solution().backspaceCompare2("abc#","bac#"))