from typing import List
class Solution:
    # simply iterate all p, and count the probabilities
    # e.g. [0.5,0.5,0.5]
    # 1st [0.5, 0.5]
    # 2nd [0.25, 0.25+0.25=0.5, 0.25]
    # 3rd [0.125, 0.125+0.25, 0.25+0.125, 0.125]
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        cnt = [1]
        for i in range(len(prob)):
            p = prob[i]
            tmp = [cnt[0]*(1-p)]
            for j in range(target+1):           # only count till target
                a, b = cnt[j]*p, cnt[j+1]*(1-p) if j+1 < len(cnt) else 0
                # print('j:', j)
                tmp.append(a+b)
            cnt = tmp
        # print('cnt:',cnt)
        return cnt[target]

print(Solution().probabilityOfHeads([0.4],1))
print(Solution().probabilityOfHeads([0.5,0.5,0.5,0.5,0.5],0))