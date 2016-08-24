"""
125. Valid Palindrome

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True

        temp = self.filter(s.lower())
        if not temp: return True

        i = 0
        isPalin = True
        while isPalin and i<=len(temp)/2:
            if temp[i] != temp[-i-1]:
                isPalin = False
            i += 1

        return isPalin

    def filter(self, strs):
        valids = []
        val = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for character in strs:
            if character in val:
                valids.append(character)
        return valids