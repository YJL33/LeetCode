"""
https://leetcode.com/problems/string-compression/
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # if not chars: return 0
        res, cnt = [chars[0]], 1

        for c in chars[1:]:
            if c == res[-1]:
                cnt += 1
            else:
                if cnt > 1:         # add digits
                    strcnt = str(cnt)
                    for x in strcnt:
                        res += x,
                res += c,
                cnt = 1

        if cnt > 1:
            strcnt = str(cnt)
            for x in strcnt:
                res += x,

        for i in range(len(res)):
            chars[i] = res[i]

        return len(res)

print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))