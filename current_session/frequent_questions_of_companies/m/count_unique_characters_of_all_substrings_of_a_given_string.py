# for non repetitive string:
# e.g. 
# "abc" => 1+ 1+2+ 1+2+3 = 10
# "aab" => 1+ 1+0+ 1+2+1 = 6            a: (0,1) => -2*2            -4
# "aaa" => 1+ 1+0+ 1+0+0 = 3            a: (0,1,2) => -2*2+-3*1     -7
# "aba" => 1+ 1+2+ 1+2+1 = 8            a: (0,2) => -1*2            -2
# "abaa" => 1+ 1+2+ 1+2+1+ 1+0+1+0 = 10 a: (0,2,3) => -2-2-2-4      -10

# "ab" => 1+ 1+2 = 4
# "abcd" => 1+ 1+2+ 1+2+3+ 1+2+3+4 = 20
# "abcde" => 1+ 1+2+ 1+2+3+ 1+2+3+4+ 1+2+3+4+5 = 35

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        N = len(s)
        if N == len(set(s)):
            return sum([i*(N+1-i) for i in range(1,N+1)])
        
        # store the previous head and tail
        print('given:', s)
        res, lastDP = 0, 0
        letters = [[-1, -1] for _ in range(26)]     # (1st right, 2nd right)
        for i in range(len(s)):
            print('i, lastDP, res', i, lastDP, res)
            a, b = letters[ord(s[i])-ord('a')]
            lastDP += i-2*a+b
            res += lastDP
            letters[ord(s[i])-ord('a')] = [i, a]
        
        return res%(10**9+7)

print(Solution().uniqueLetterString('a'))
print(Solution().uniqueLetterString('ab'))
print(Solution().uniqueLetterString('aba'))
print(Solution().uniqueLetterString('aab'))
print(Solution().uniqueLetterString('abc'))
print(Solution().uniqueLetterString('abcd'))
print(Solution().uniqueLetterString('abcde'))
print(Solution().uniqueLetterString('abaa'))
