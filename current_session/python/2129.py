class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        res = []
        for w in words:
            tmp = ""
            if len(w) <= 2:
                tmp = w.lower()
            else:
                tmp = w[0].upper() + w[1:].lower()
            res.append(tmp)
        return " ".join(res)