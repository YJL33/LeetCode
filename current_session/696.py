class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # simply go through the whole string and keep a 'prev' and 'prev length'
        prev = None
        cnt = {'0':0, '1':0}
        res = 0
        for i in range(len(s)):
            if not prev or s[i] != prev:
                prev = s[i]
                res += min(cnt.values())
                cnt[s[i]] = 1
            else:
                cnt[s[i]] += 1
        return res+min(cnt.values())
            
print(Solution().countBinarySubstrings('10101'))
print(Solution().countBinarySubstrings('00110011'))
print(Solution().countBinarySubstrings('0000001'))
print(Solution().countBinarySubstrings('10000001'))
print(Solution().countBinarySubstrings('1000000111000111'))
