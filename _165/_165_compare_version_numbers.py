"""
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # compare first-level, if same, compare second-level
        return self.helper(version1, version2)

    def helper(self, version1, version2, s1=0, s2=0):
        #print s1, s2
        num1 = num2 = 0
        p1, p2 = len(version1), len(version2)
        for i in xrange(s1, len(version1)):
            if version1[i] in '0123456789':
                num1 = num1*10 + int(version1[i])
            elif version1[i] == '.':
                p1 = i
                break

        for j in xrange(s2, len(version2)):
            if version2[j] in '0123456789':
                num2 = num2*10 + int(version2[j])
            elif version2[j] == '.':
                p2 = j
                break

        if num1-num2 > 0:
            return 1
        elif num1-num2 < 0:
            return -1
        else:
            if p1 == len(version1) and p2 == len(version2):
                return 0
            return self.helper(version1, version2, p1+1, p2+1)