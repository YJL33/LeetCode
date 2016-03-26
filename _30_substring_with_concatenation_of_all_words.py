"""
30. Substring with Concatenation of All Words
Total Accepted: 51856 Total Submissions: 250868 Difficulty: Hard

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s
that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLength = len(words[0])
        numOfWords = len(words)
        if numOfWords is 0:     # No need to return anything
            return

        wordDict = {}           # Construct a dictionary to save the index of word.
        for w in words:
            if w not in wordDict:
                wordDict[w] = 1
            else:
                wordDict[w] += 1        # words that appeared more than once in the list

        outputList = []                 # Final output
        for i in xrange(len(s)-wordLength*numOfWords+1):
            seenWordDict = wordDict.copy()
            for j in xrange(numOfWords):
                substring = s[i+j*wordLength:i+(j+1)*wordLength]
                if substring not in words:
                    break
                seenWordDict[substring] -= 1
                if seenWordDict[substring] < 0:
                    break
                if j == numOfWords-1:
                    outputList.append(i)
        return outputList
