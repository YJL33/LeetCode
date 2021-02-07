import collections
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        rows = input.split('\n')
        subDirs = collections.defaultdict(int)
        maxSeen = 0
        for r in rows:
            # check depth (i)
            i = 0  
            while r[i:i+1] == '\t':
                i += 1
            # check Filename Extension
            if '.' not in r:
                # do nothing, just add it into subDirs
                subDirs[i] = len(r[i:])
            else:
                # check the abs path
                lenOfAbsPath = len(r[i:])
                while i > 0:
                    lenOfAbsPath += subDirs[i-1] + 1
                    i -= 1
                maxSeen = max(maxSeen, lenOfAbsPath)
            # print r
            # print subDirs, maxSeen
        return maxSeen

print Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print Solution().lengthLongestPath("a")
print Solution().lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")