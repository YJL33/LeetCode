# simply go through the whole string twice
class Comparer:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = self._helper(s)
        b = self._helper(t)
        return a == b
    
    def _helper(self, s):
        res = []
        for i in range(len(s)):
            if s[i] != "#":
                res.append(s[i])
            else:
                if res: res.pop()
        return "".join(res)

print(Comparer().backspaceCompare("ab#c", "ad#c"))
print(Comparer().backspaceCompare("ab##", "c#d#"))
print(Comparer().backspaceCompare("a##c", "#a#c"))
print(Comparer().backspaceCompare("a#c", "b"))