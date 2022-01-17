class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # check the number of continous A and Bs
        cnt = {"A":0, "B":0}
        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                cnt[colors[i]] += 1
        return cnt["A"] > cnt["B"]
