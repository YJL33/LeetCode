"""
1209
"""
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if not stack or s[i] != stack[-1][0]:
                stack.append((s[i], 1))
            else:
                char, cnt = stack.pop()
                if cnt+1 == k: continue
                stack.append((char, cnt+1))
        return ''.join([a*b for a,b in stack])

print(Solution().removeDuplicates("pbbcggttciiippooaais", 2))
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))