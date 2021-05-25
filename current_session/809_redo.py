"""
https://leetcode.com/problems/expressive-words/
"""
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for w in words:
            ans += self.check(w, S)
        return ans

    def check(self, w, s):
        # use 2 pointers
        p1, p2 = 0, 0
        while p1 < len(w) and p2 < len(s):
            if w[p1] != s[p2]:
                return False
            # stretch here
            else:
                c1, c2 = 1,1
                while p1+c1 < len(w) and w[p1] == w[p1+c1]:
                    c1 += 1
                while p2+c2 < len(s) and s[p2] == s[p2+c2]:
                    c2 += 1
                # note that we can only stretch w
                if c1 != c2 and c2 < max(c1, 3):
                    return False
                p1, p2 = p1+c1, p2+c2
        return p1 == len(w) and p2 == len(s)

print(Solution().expressiveWords(S = "heeellooo",words = ["hello", "hi", "helo"]))