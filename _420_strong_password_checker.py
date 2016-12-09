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
        length, repeat, i, j, counter = len(s), [], 0, 1, [0]*4     # refer to classifier

        while i < length:
            while i+j < length and s[i+j] == s[i]: j += 1
            if j >= 3: repeat += (j, s[i]),                         # get repeats
            counter[self.classifier(s[i])] += j                     # count lower/upper/digit
            i, j = i+j, 1

        insert, delete, replace, flag = 0, 0, 0, (6 <= length <= 20)

        while length < 6:                           # case A: (L<6)
            length, insert = length+1, insert+1     # at least 1 insert => no need to fix repeat
            counter[counter.index(min(counter[:-1]))] += 1      # NOTE: insert the missing one

        if length > 20:                             # case B: (L>20) fix repeat by delete & replace
            delete, candel = length-20, sum([r[0]-2 for r in repeat])
            if delete < candel:                     # (replace + delete) MUST >= len(repeat)
                replace = max(len(repeat)-delete, ((candel-delete)+2)//3)

        while flag and repeat:                      # case C: (6<=L<=20) fix repeat only by replace
            replace += repeat.pop()[0]//3
                                                    # final check: if missing still > replace
        if replace < counter[:-1].count(0): replace += counter[:-1].count(0)-replace

        return replace+delete+insert

    def classifier(self, c):
        if c.islower():
            return 0
        elif c.isupper():
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3        # None of above