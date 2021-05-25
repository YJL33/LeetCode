"""
71
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        cpath = []
        prev = None
        i = 0
        while i <= len(path):
            j = i+1
            while j < len(path) and path[j] != '/':
                j += 1
            
            if j-i != 1:                            # handle //
                if path[i+1:j] == '..':             # handle ../
                    if len(cpath) > 0:
                        cpath.pop()
                elif path[i+1:j] != '.':         # handle ./
                    cpath.append(path[i+1:j])       # normal case
            i = j
        
        return '/' + '/'.join(cpath)
