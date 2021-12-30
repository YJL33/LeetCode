import collections
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # O(n)
        last_seen_vowels = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
        cnt = 0
        last_non_vowel = -1
        for i in range(len(word)):
            c = word[i]
            if c not in last_seen_vowels:
                last_non_vowel = i
            else:
                last_seen_vowels[c] = i
                cnt += max(min(last_seen_vowels.values())-last_non_vowel, 0)
        return cnt

    def countVowelSubstrings_2(self, word: str) -> int:
        # brute force
        # for all vowels word[i], try all substrings starting from i
        cnt = 0
        for i in range(len(word)):
            if word[i] not in 'aeiou':
                continue
            vc = collections.Counter()              # vowel counter
            for j in range(i, len(word)):
                if word[j] not in 'aeiou':
                    break
                if word[j] in vc:
                    vc[word[j]] += 1
                else:
                    vc[word[j]] = 1
                if all([vc['a'] > 0, vc['e'] > 0, vc['i'] > 0, vc['o'] > 0, vc['u'] > 0]):
                    cnt += 1
                    # print('cnt:', cnt, i, j)
        return cnt

print(Solution().countVowelSubstrings("aeiouu"))
print(Solution().countVowelSubstrings("unicornarihan"))
print(Solution().countVowelSubstrings("poazaeuioauoiioaouuouaui"))
