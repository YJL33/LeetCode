"""
131. Palindrome Partitioning

Given a string s,
partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # implement backtracking
        res = []
        self.helper(s, res)
        return res

    def helper(self, string, res, path=[]):
        if string == '':                # if nothing left
            res.append(path)            # add it into result
            return

        for i in xrange(1, len(string)+1):
            if self.isPalindrome(string[:i]):                       # this part is valid
                self.helper(string[i:], res, path+[string[:i]])     # keep check the rest

    def isPalindrome(self, s):
        # check whether this string is palindrome or not
        for i in xrange(len(s)/2):
            if s[i] != s[-i-1]:
                return False
        return True

print Solution().partition("aab")