"""
388. Longest Absolute File Path

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains:
an empty sub-directory subdir1, and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to file in the abstracted file system.
If there is no file in the system, return 0.

Note:

    The name of a file contains at least a . and an extension.
    The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path,
if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""
class Solution(object):
    def lengthLongestPath(self, log):
        """
        :type log: str
        :rtype: int
        """
        if not log: return 0
        # First scan all structure and record folder depth/position/range and file position

        length = len(log)
        separator = [-1]

        for i in xrange(length):
            if log[i] == '\n':                  # something in between!
                separator.append(i)

        separator.append(length)

        files = []                              # file and folders are represented as triple
        folders = []                            # e.g. 'root' (layer = 0, index = 0, sublength = 4)
        for j in xrange(len(separator)-1):
            head, tail = separator[j], separator[j+1]
            sublen = tail-head-1                # not including backslash
            index = head+1
            layer = 0
            isFile = False
            for k in xrange(head+1, tail):
                if log[k] == '\t':
                    sublen -= 1
                    index += 1
                    layer += 1
                elif log[k] == '.':
                    isFile = True
            if isFile:
                files += (layer, index, sublen),
            else:
                folders += (layer, index, sublen),
        #print files, folders
        res = [0]
        for f in files:
            res.append(self.findFilePath(f, folders))

        return max(res)

    def findFilePath(self, f, folders):
        # Find this file's directory and return it's path length
        #print f,
        file_layer = f[0]
        pos = f[1]
        pathlen = f[2]

        for fo in folders[::-1]:
            if fo[0] < file_layer and fo[1] < pos:
                #print fo,
                pathlen += fo[2] + 1            # add backslash
                file_layer -= 1
        #print '\n'
        return pathlen