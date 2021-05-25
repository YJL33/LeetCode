class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        for i in xrange(len(t)):
            if j < len(s) and t[i] == s[j]:
                # print "what now:", t[i], s[j]
                j += 1
        
        return j == len(s)

print Solution().isSubsequence("abc", "ahbgdc"), "should be True"
print Solution().isSubsequence("axc", "ahbgdc"), "should be False"
print Solution().isSubsequence("abc", "abc"), "should be True"
print Solution().isSubsequence("aaa", "aaaa"), "should be True"
print Solution().isSubsequence("aaa", "aa"), "should be False"
print Solution().isSubsequence("a", "jpqobiwjpehqpierihqpiwherphqkkwea"), "should be True"
print Solution().isSubsequence("querta", "qwerty"), "should be False"