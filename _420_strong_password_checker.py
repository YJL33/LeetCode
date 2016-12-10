"""
420. Strong Password Checker

    Total Accepted: 977
    Total Submissions: 4546
    Difficulty: Hard
    Contributors: yduan7

A password is considered strong if below conditions are all met:

    It has at least 6 characters and at most 20 characters.
    It must contain at least one lowercase letter, one uppercase letter, and one digit.
    It must NOT contain three repeating characters in a row
    ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input,
and return the MINIMUM change required to make s a strong password.

If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, repeat, types, i, j = len(s), [], [False]*4, 0, 1

        while i < length:
            while i+j < length and s[i+j] == s[i]: j += 1
            if j >= 3: repeat += j,                     # get repeats
            types[self.classifier(s[i])] = True         # check lower/upper/digit
            i, j = i+j, 1

        insert, delete, replace = 0, 0, 0
        
        if length < 6: insert = 6-length                # Case A.
        
        elif length > 20:   # Case B. Fix repeat by (replace+delete), should > all solve by replace
            delete, allbydel = length-20, sum([r-2 for r in repeat])
            if delete < allbydel:
                replace = max(sum([r//3 for r in repeat])-delete, ((allbydel-delete)+2)//3)

        else:               # Case C. fix repeat only by replace
            for rp in repeat: replace += rp//3

        # final check: if replace less than missing
        return insert+delete+max(replace, types[:-1].count(False)-insert)

    def classifier(self, c):
        # types: 0 = lowercase, 1 = uppercase, 2 = digit, 3 = others (None of above)
        if c.islower(): return 0
        elif c.isupper(): return 1
        elif c.isdigit(): return 2
        else: return 3