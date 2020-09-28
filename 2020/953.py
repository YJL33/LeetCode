"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            if self.compare(words[i], words[i+1], order) is False:
                return False

        return True
    
    def compare(self, A, B, order):
        for i in range(len(A)):

            # move to the end
            # if i >= len(A):
            #     return True

            if i >= len(B):
                return False

            a, b = A[i], B[i]

            if a == b:
                continue
            elif order.index(a) > order.index(b):
                return False
            else:
                return True

        return True

print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
print(Solution().isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz"))
