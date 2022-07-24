class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        return haystack.find(needle)
    
    # def strStr(self, A, B) -> int:
    #     if not B: return 0
    #     L = len(B)
    #     for i in range(len(A)):
    #         a = A[i]
    #         if a == B[0]:
    #             if A[i:i+L] == B: return i
    #     return -1


print(Solution().strStr("hello","ll"))
print(Solution().strStr("aaaaaaa","bba"))
print(Solution().strStr("aaaaaaa",""))