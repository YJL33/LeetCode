"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # naive approach: identify the chars and remove
        # keep checking until no chars identified

        # O(n)
        # use stack
        # for each c in s:
        # if it's as same as prev: cnt+=1
        # if cnt == k:       
        # else: add new char

        i,stack = 1,[(s[0],1)]
        while i<len(s):
            if len(stack):
                prev, cnt = stack.pop()
            if s[i] == prev:
                cnt += 1
                if cnt < k:
                    stack += (prev, cnt),
            else:
                if cnt < k:
                    stack += (prev, cnt),
                elif cnt > k:
                    stack += (prev, cnt-k),
                stack += (s[i], 1),
            i += 1
        return ''.join([a[0]*a[1] for a in stack])


print(Solution().removeDuplicates("pbbcggttciiippooaais", 2))
print(Solution().removeDuplicates("deeedbbcccbdaa", 3))
