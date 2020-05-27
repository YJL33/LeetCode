"""
 5. Longest Palindromic Substring

    Total Accepted: 169798
    Total Submissions: 686389
    Difficulty: Medium
    Contributors: Admin

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    """Solution of leetcode #5"""
    def longestPalindrome(self, word):
        """
        :type word: str
        :rtype: str
        """
        maxsub, count, wordlen = "", 0, len(word)
        for i in range(wordlen):
            start = end = i
            if (end + count/2) > len(word):
                break
            # check even
            if word[i] == word[i-1]:
                start -= 1
                while start >= 0 and end < len(word) and word[start] == word[end]:
                    start, end = start-1, end+1
            # check odd
            start2 = end2 = i
            while start2 >= 0 and end2 < len(word) and word[start2] == word[end2]:
                start2, end2 = start2-1, end2+1
            # compare
            if end2-start2 > end-start:
                start, end = start2, end2
            if end-start+1 > count:
                maxsub, count = word[start+1:end], end-start+1

        return maxsub

# def main():
#     """ code here """
#     wordlist = ["babad", "a",
#                 "uriowsiuwrhroiwhfooxooxxoxookkkkkkkfjshpopopopopopopopopiiiiiiipopopopojjjjjj"]
#     print map(Solution().longestPalindrome, wordlist)

# if __name__ == "__main__":
#     main()
