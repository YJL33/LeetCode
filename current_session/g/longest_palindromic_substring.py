# longest palindromic substring
# the naive approach: try all i, j and check S[i:j] is palindrome or not
# time complexity: O(n^3)
# we should be able to leverage DP
# s[i:j] is palindrome if s[i+1:j-1] and s[i] == s[j]
# use DP to store local solution
# time complexity: (try all i, j) O(n^2)
# another approach:
# for each s[i], check whether there's a palindrome using s[i] as center
# check both even and odd
# time complexity: O(n^2)

class Solution:
    def longestPalindrome(self, s):
        def checker(l, r):
            while 0<=l-1 and r+1<len(s) and s[l-1]==s[r+1]:
                l, r = l-1, r+1
            return s[l:r+1]

        res = ""
        for i in range(len(s)):
            a, b = "", checker(i, i)
            if i+1 < len(s) and s[i] == s[i+1]:
                a = checker(i, i+1)
            # print('even and odd:', a, " ", b, "   i=",i)
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
        return res
    
    def longestPalindrome_ON(self,s):
        # leverage manacher's algorithm
        def getMS():
            return "^#" + ''.join([c+"#" for c in s]) + "$"

        ms = getMS()
        # print(ms)

        def finder(i):
            l, r, cnt = i, i, 0
            while 0<=l-1 and r+1 < len(ms) and ms[l-1] == ms[r+1]:
                l, r, cnt = l-1, r+1, cnt+1
            return cnt
        
        res = [0 for _ in range(len(ms))]
        center, radius, lpr = 0, 0, ""
        for i in range(len(ms)):
            mirror = 2*center-i
            if (radius > i and mirror >= 1 and (i+res[mirror] < radius)):
                res[i] = res[mirror]
                continue
            res[i] = finder(i)
            center, radius = i, i+res[i]

            # update LPR
            if res[i] > len(lpr):
                r = res[i]//2
                if ms[i] != "#":
                    lpr = [ms[j] for j in range(i-r*2, i+r*2+1, 2)]
                else:
                    lpr = [ms[j] for j in range(i-r*2+1, i+r*2, 2)]
                # print('lpr',lpr)
        
        # print('res', res)
        print(res)
        return ''.join(lpr)

print(Solution().longestPalindrome_ON("bab"))
print(Solution().longestPalindrome_ON("cbbd"))
print(Solution().longestPalindrome_ON("a"))
print(Solution().longestPalindrome_ON("ccd"))
print(Solution().longestPalindrome_ON("babad"))

