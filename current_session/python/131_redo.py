from typing import List
class Solution:

    def partition_bruteforce(self, s: str) -> List[List[str]]:
        res = []
        for i in range(1, len(s)+1):
            for rest in self.partition(s[i:]):
                if s[:i] == s[i-1::-1]:
                    res.append([s[:i]]+rest)
        return res if res != [] else [[]]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, res)
        return res

    def helper(self, string, res, path=[]):
        if string == '':                # if nothing left
            res.append(path)            # add it into result
            return

        for i in range(1, len(string)+1):
            if self.isPalindrome(string[:i]):                       # this part is valid
                self.helper(string[i:], res, path+[string[:i]])     # keep check the rest
        return

    def isPalindrome(self, s):
        # check whether this string is palindrome or not
        for i in range(len(s)/2):
            if s[i] != s[-i-1]:
                return False
        return True