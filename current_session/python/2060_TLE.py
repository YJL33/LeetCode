import collections
class Solution:
    def possiblyEquals_TLE(self, s1: str, s2: str) -> bool:
        # count the length of string (handle numbers) and get the possible lengths
        # if there's any length that's possible on set s1 and set s2,
        # check the alphabetic orders
        # e.g. 123 -> 1,2,3 | 12, 3 | 1, 23 | 123

        def get_numbers(s, i):
            # get the end first
            j = i+1
            while j < len(s) and s[j].isdigit():
                j += 1
            # now we handle s[i:j]
            substr = s[i:j]
            # print('substr', substr)
            L = j-i-1
            # print('L', L)
            # we should have 2^L possible numbers
            # craft the substring based on L
            # and then convert to number
            res = []
            while len(res) < pow(2, L):
                x = len(res)
                tmp = ["" for _ in range(2*L+1)]
                for i in range(1, 2*L+1, 2):
                    if x%2: tmp[i] = ","
                    x = x//2
                for k in range(0,2*L+1, 2):
                    tmp[k] = substr[k//2]
                tmp = [y for y in tmp if y != '']
                # print('tmp:', tmp)
                carry = 0
                lengthSum = 0
                for t in tmp:
                    if t != ',':
                        carry = carry*10+int(t)
                    else:
                        lengthSum += carry
                        carry = 0
                lengthSum += carry
                # print('lengthSum', lengthSum)
                res.append(lengthSum)
            return res, j

        def get_pos(s1):
            pos = []
            i = 0
            while i < len(s1):
                if not s1[i].isdigit():
                    pos.append([1])
                    i += 1
                else:
                    comb, i = get_numbers(s1, i)
                    pos.append(comb)
            dp = [[x] for x in pos[0]]
            for p in pos[1:]:
                tmp = []
                for prev in dp:
                    for cur in p:
                        tmp.append(prev + [cur])
                dp = tmp
            return dp

        pos1 = get_pos(s1)
        pos2 = get_pos(s2)

        def get_dd(pos):
            dd = collections.defaultdict(list)
            for i in range(len(pos)):
                p = pos[i]
                dd[sum(p)].append(i)
            return dd

        ddict1 = get_dd(pos1)
        ddict2 = get_dd(pos2)

        union = set(ddict1.keys()).intersection(ddict2.keys())
        if len(union) == 0: return False
        # print('union:', union)

        if set(s1).issubset(set('123456789')) or set(s2).issubset(set('123456789')): return True

        def get_sd(arr, s):
            sd = {}
            index, index_s = 0, 0
            for a in arr:
                if a == 1 and s[index_s] not in '123456789':
                    sd[index] = index_s
                    index += 1
                    index_s += 1
                else:
                    index += a
                    while index_s < len(s) and s[index_s] in '123456789':
                        index_s += 1
            return sd

        for u in union:
            for c1 in ddict1[u]:
                for c2 in ddict2[u]:
                    a, b = pos1[c1], pos2[c2]
                    ad, bd = get_sd(a, s1), get_sd(b, s2)
                    uu = set(ad.keys()).intersection(bd.keys())
                    # print('uu', uu)
                    # print('ad', ad)
                    # print('bd', bd)
                    if len(uu) == 0: return True
                    is_all_match = True
                    for uuu in uu:
                        if ad[uuu] != bd[uuu]:
                            is_all_match = False
                            break
                    if is_all_match: return True
        return False
        
# print(Solution().possiblyEquals_TLE("internationalization", "i18n"), 't')
# print(Solution().possiblyEquals_TLE("l123e", "44"), 't')
# print(Solution().possiblyEquals_TLE("ab","a2"), 'f')
# print(Solution().possiblyEquals_TLE("giejrqhftbrwnkqiwtnxcuggjaucanteswgpfmqq","1iejrqhftbrwnkqiwtnxcuggjaucanteswgpfmqq"), 't')
# print(Solution().possiblyEquals_TLE("v853u344u9u8v838v726v78","v2v61v36v48u47v337v6v32"), 't')
# print(Solution().possiblyEquals_TLE("a5b","c5b"), 'f')
print(Solution().possiblyEquals_TLE("98u8v8v8v89u888u998v88u98v88u9v99u989v8u","9v898u98v888v89v998u98v9v888u9v899v998u9"))

