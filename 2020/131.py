"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

"""
class Solution(object):

    # partition all gap and check both side
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, res)
        return res

    def helper(self, substring, res, temp=[]):
        if substring == '':
            res.append(temp)
            return

        for i in xrange(1, len(substring)+1):
            left, right = substring[:i], substring[i:]
            print "L:", left, "R:", right
            if self.isPalindrome(left):
                self.helper(right, res, temp+[left])

    def isPalindrome(self, substring):
        for i in xrange(len(substring)/2):
            if (substring[i] != substring[-i-1]):
                return False
        return True

# print Solution().partition("aab")
print Solution().partition("aabaa")