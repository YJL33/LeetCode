# by observation:
# if count == 1: delete this -> reduce compressed length by 1
# if count == 2: delete 1 -> reduce compressed length by 1
#                delete 2 -> reduce compressed length by 2
# if count == 3: delete 1 -> no reduce
#                delete 2 -> reduce compressed length by 1
#                delete 3 -> reduce compressed length by 2
# ...
# if count == 10: delete 1 -> reduce compressed length by 1
#                 delete 2 -> reduce compressed length by 1
# ...             delete 9 -> reduce compressed length by 2
# ...             delete 10 -> reduce compressed length by 3
# if count == 100: delete 1 -> reduce compressed length by 1
#                  delete 2 -> reduce compressed length by 1
# ...              delete 90 -> reduce compressed length by 1
# ...              delete 91 -> reduce compressed length by 2
# ...              delete 99 -> reduce compressed length by 3
# ...              delete 100 -> reduce compressed length by 4
#
# consider edge cases:
# aabbaa

from functools import lru_cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, lastChar, lastCharCnt, left):
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == lastChar:        # repeat char, no delete
                incr = 1 if lastCharCnt in [1,9,99] else 0
                return incr + counter(start+1, lastChar, lastCharCnt+1, left)
            else:
                keep = 1 + counter(start+1, s[start], 1, left)
                remove = counter(start+1, lastChar, lastCharCnt, left-1)
                return min(keep, remove)

        return counter(0, "", 0, k)

print(Solution().getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
print(Solution().getLengthOfOptimalCompression(s = "aabbaa", k = 2))
print(Solution().getLengthOfOptimalCompression(s = "aaaaaaaaaaa", k = 0))
