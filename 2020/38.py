class Solution:
    def countAndSay(self, n: int) -> str:
        res = (1,'1')       # res[i] is the nth-seq to 'say'
        if n == 0: return

        def say(x: str) -> str:
            output, cnt, i = "", 0, 0
            while i < len(x):
                cnt += 1
                if i+1 == len(x) or x[i] != x[i+1]:
                    output += str(cnt)+x[i]
                    cnt = 0     # it'll be fine to reset the counter when i+1=len(x)
                i += 1
            return output

        while res[0] < n:
            res = (res[0]+1, say(res[1]))
        return res[-1]

print(Solution().countAndSay(1))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))
print(Solution().countAndSay(10))
# print(Solution().countAndSay(4))
