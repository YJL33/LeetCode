"""
318. Maximum Product of Word Lengths

Given a string array words,
find the maximum value of length(word[i]) * length(word[j]),
where the two words do not share common letters.

You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:

Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:

Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:

Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # implement bit manipulation (can be improved into 2 lines)
        dct = {}
        words.sort(key=len)

        for w in words:
            tmp = 0
            for c in set(w):
                tmp += 1<<(ord(c)-97)
            dct[tmp] = len(w)

        res = 0
        for k, v in dct.items():
            for K, V in dct.items():
                if not k&K:
                    res = max(res, v*V)

        return res
