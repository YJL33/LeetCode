class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num)-1
        while l < r:
            if num[l] == "9" and num[r] != "6": return False
            elif num[l] == "6" and num[r] != "9": return False
            elif num[l] == "8" and num[r] != "8": return False
            elif num[l] == "0" and num[r] != "0": return False
            elif num[l] == "1" and num[r] != "1": return False
            elif num[l] in "23457" or num[r] in "23457": return False
            else:
                l, r = l+1, r-1
        return num[l] in "018" if l == r else True