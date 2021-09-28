from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # if find // go to next row
        # if find /* find next */
        res = []
        inBlock = False
        for r in source:
            tmp = '' if not inBlock else tmp        # keep it into next res addition
            # find comment sign in each row
            i = 0
            while i < len(r):
                if not inBlock and r[i:i+2] == "//":
                    # tmp.append()
                    break
                elif not inBlock and r[i:i+2] == "/*":
                    inBlock = True
                    i += 2
                elif inBlock and r[i:i+2] == "*/":
                    inBlock = False
                    i += 2
                else:
                    if not inBlock: tmp += r[i]
                    i += 1
            
            if not inBlock and tmp != '':
                res.append(tmp)
        
        return res

print(Solution().removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))