class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # simply use dict
        n = len(pattern)
        words = s.split()
        if len(words) != n or len(set(words)) != len(set(pattern)): return False
        pattern_dict = {}           # key: pattern, value: word
        for i in range(n):
            w = words[i]
            p = pattern[i]
            if p not in pattern_dict:
                pattern_dict[p] = w
            else:
                if pattern_dict[p] != w: return False
        return True