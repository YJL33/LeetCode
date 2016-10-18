"""
 65. Valid Number

    Total Accepted: 55551
    Total Submissions: 445158
    Difficulty: Hard
    Contributors: Admin

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument,
please click the reload button to reset your code definition.
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Lack of info.
        def isZeroToNine(char):
            #assert len(char) == 1
            return (ord(char) >= 48 and ord(char) <= 57)

        def dotChecker(i):
            # return this dot is valid or not
            if (i != 0 and isZeroToNine(s[i-1])) and (i == len(s)-1 or (s[i+1]) == ' '):
                return True and e != 1      # 5.
            elif not anydigit and (i != len(s)-1 and isZeroToNine(s[i+1])):
                return True and e != 1      # .5
            elif (i != 0 and isZeroToNine(s[i-1])) and (i != len(s)-1 and s[i+1] in '0123456789e'):
                return True and e != 1      # 5.5
            return False

        if not s: return False
        e = 0
        anydigit, nomoredigit, nomoredot, nomoresign = False, False, False, False

        for i in xrange(len(s)):
            c = s[i]
            if not isZeroToNine(c):
                if c in '+-':                       # +/-
                    if nomoresign: return False
                    elif (e == 1 or not anydigit) and (i < len(s)-1 and s[i+1] in '.0123456789'):
                        nomoresign = True
                        continue
                    return False
                elif ord(c) == 32:                  # space must exist before or after number
                    if not anydigit: continue
                    nomoredigit = True
                elif ord(c) == 46:                  # dot must have number before or after it
                    if nomoredot or not dotChecker(i): return False
                    nomoredot = True
                elif ord(c) == 101:                 # e
                    e += 1
                    if e > 1: return False          # e must appear only once
                    if (i != 0 and s[i-1] in '0123456789.') and (i != len(s)-1 and s[i+1] in '0123456789+-'):
                        nomoresign = False          # 
                        continue
                    return False                    # e must have number after it
                else:
                    return False
            else:
                if nomoredigit: return False
                anydigit = True
                    
        return anydigit

