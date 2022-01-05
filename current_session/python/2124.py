class Solution:
    def checkString(self, s: str) -> bool:
        max_a, min_b = 0, len(s)-1
        for i in range(len(s)):
            if s[i] == 'a':
                max_a = i
            else:
                min_b = min(min_b, i)
            if max_a > min_b:
                return False
        return True