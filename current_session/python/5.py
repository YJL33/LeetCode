# longest palindromic substring
#
# dumbest approach: try all i, j and check S[i:j] is palindrome or not
# time complexity: O(n^3)
#
# naive approach
# for each s[i], check whether there's a palindrome using s[i] as center
# check both even and odd
# time complexity: O(n^2)
#
# leverage DP
# s[i:j] is palindrome if s[i+1:j-1] and s[i] == s[j]
# use DP to store local solution
# time complexity: (try all i, j) O(n^2)
#
# implement manacher's algorithm
# time complexity: O(n)
class Solution:
    # use dp
    # dp[i][j] = True if s[i:j] is palindrome
    # note that bool(-1) == True
    def longestPalindrome_dp(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        maxLen, start, end = 0, 0, 0
        for i in range(len(s), -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j] and j-i > maxLen:
                    # print('True: i, j', i, j, s[i:j+1])
                    maxLen, start, end = j-i, i, j
        
        return s[start:end+1]

    # try each character as middle position of palindrome
    # use 2 cursors, check left and right
    def longestPalindrome_naive(self, s):
        def checker(l, r):
            while 0<=l-1 and r+1<len(s) and s[l-1]==s[r+1]:
                l, r = l-1, r+1
            return s[l:r+1]
        lpr = ""
        for i in range(len(s)):
            for isEven in [0,1]:            # check twice
                a = ""
                if isEven == 0:
                    a = checker(i, i)
                elif i+1 < len(s) and s[i] == s[i+1]:
                    a = checker(i, i+1)
                if len(a) > len(lpr): lpr = a
        return lpr

    # leverage manacher's algorithm
    def longestPalindrome(self, s):
        def getMS():
            return "^#" + ''.join([c+"#" for c in s]) + "$"

        ms = getMS()

        def finder(i):
            l, r, cnt = i, i, 0
            while 0<=l-1 and r+1 < len(ms) and ms[l-1] == ms[r+1]:
                l, r, cnt = l-1, r+1, cnt+1            # with "#" cnt will be lengthOfLPR
            return cnt
        
        lengthOfLPR = [0 for _ in range(len(ms))]      # Length of LPR
        center, radius, lpr = 0, 0, ""
        for i in range(len(ms)):
            mirror = 2*center-i
            if (radius > i and mirror >= 1 and (i+lengthOfLPR[mirror] < radius)):
                lengthOfLPR[i] = lengthOfLPR[mirror]
                continue
            lengthOfLPR[i] = finder(i)
            center, radius = i, i+lengthOfLPR[i]

            # update LPR
            if lengthOfLPR[i] > len(lpr):
                r = lengthOfLPR[i]//2
                if ms[i] != "#":
                    lpr = [ms[j] for j in range(i-r*2, i+r*2+1, 2)]
                else:
                    lpr = [ms[j] for j in range(i-r*2+1, i+r*2, 2)]
        
        print('ms', ms)
        print('lengthOfLPR', lengthOfLPR)
        return ''.join(lpr)


print(Solution().longestPalindrome("abcda"), "a")
print(Solution().longestPalindrome("abccba"), "abccba")
print(Solution().longestPalindrome("aaaaaaaaaaa"), "aaaaaaaaaaa")
print(Solution().longestPalindrome("abba"), "abba")
print(Solution().longestPalindrome("ac"), "a")
print(Solution().longestPalindrome(""), "")

print(Solution().longestPalindrome("bab"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ccd"))
