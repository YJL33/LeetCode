"""
https://leetcode.com/problems/string-compression/
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars: return 0
        output = []
        prev = chars[0]
        cnt = 0
        for i in range(len(chars)):
            if chars[i] == prev:
                cnt += 1
            else:
                output += prev,
                if cnt > 1: output += self.getCntAsStr(cnt)
                prev, cnt = chars[i], 1

        output += prev,
        if cnt > 1: output += self.getCntAsStr(cnt)

        # overwrite chars
        for i in range(len(output)):
            chars[i] = output[i]

        return len(output)

    def getCntAsStr(self, cnt):     # add spliter in between
        res = []
        while cnt:
            res += str(cnt%10),
            cnt = cnt//10
        return res[::-1]


print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))