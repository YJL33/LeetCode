import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window
        # maintain a dictionary: key: character, value: last index
        # keep increase r
        #   if character s[r] is not in dictionary or last index of s[r] < l: 
        #       update character and keep l unchanged
        #   else:
        #       update l
        # maintain a max_seen window size
        if not s: return 0
        
        max_seen, l = 0, -1
        char_dict = collections.defaultdict(int)

        for r, c in enumerate(s):
            if c in char_dict and char_dict[c] >= l:
                l = char_dict[c]
            char_dict[c] = r
            max_seen = max(max_seen, r-l)
        
        return max_seen

print(Solution().lengthOfLongestSubstring("apsodifupbjapsdijfpa"))
print(Solution().lengthOfLongestSubstring(" "))
print(Solution().lengthOfLongestSubstring("abcde"))