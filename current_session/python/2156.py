class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, target: int) -> str:
        # can we use something similar to prefix?
        # first, calculate its base value
        N = len(s)
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        base = {}
        for i in range(26):
            base[alphabet[i]] = (i+1)
           
        # base_value: the number after modulo
        # calculate by shifting
        # avoid using power to get rid of TLE
        
        tmp = 0
        x = 1
        for i in range(k):
            tmp += base[s[i]]*x
            x *= p
        
        if tmp%m == target: return s[:k]
        # print('init:', tmp)
        
        for j in range(k, N):
            left = j-k
            tmp += base[s[j]]*x - base[s[left]]
            tmp = tmp//p

            if tmp%m == target:
                return s[left+1:j+1]
        
        return
        