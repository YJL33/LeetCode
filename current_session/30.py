"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s 
that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) is 0:
            return []

        wordDict = {}
        for w in words:
            if w not in wordDict:
                wordDict[w] = 1
            else:
                wordDict[w] += 1

        # the number of words and the length of each word are both known
        lengthOfWord = len(words[0])
        numOfWords = len(words)
        lengthOfSubstring = numOfWords * lengthOfWord

        res = []

        for i in xrange(len(s)):
            copyOfWordDict = wordDict.copy()
            substring = s[i:i+lengthOfSubstring]
            if len(substring) != lengthOfSubstring:
                break
            for j in xrange(numOfWords):
                w = substring[j*lengthOfWord:(j+1)*lengthOfWord]
                if w not in copyOfWordDict:
                    break
                else:
                    copyOfWordDict[w] -= 1

                if copyOfWordDict[w] < 0:
                    break
                if j == numOfWords -1:
                    res += i,

        return res

print Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
print Solution().findSubstring("barfoothefoobarman", ["foo","bar"])