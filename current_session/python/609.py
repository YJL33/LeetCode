"""
609
"""
import collections
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # simply use dictionary

        fd = collections.defaultdict(list)        
        for i in range(len(paths)):
            files = paths[i].split()
            for f in files[1:]:
                meta1, meta2 = f.split('(', 1)
                path = files[0] + "/" + meta1
                content = meta2[:-1]
                fd[content].append(path)
        # print fd
        return [a for a in fd.values() if len(a)>=2]