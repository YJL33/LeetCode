"""
see https://leetcode.com/problems/remove-comments/
"""
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # naive approach
        # handle each row
        # if see /*, find next */
        # if see //, go next row
        # else add into tmp
        inBlock = False
        res = []
        tmp = ''
        for row in source:
            i = 0
            tmp = '' if not inBlock else tmp    # special case
            # print('row',row)
            while i < len(row):
                if inBlock:
                    end = row[i:].find('*/')
                    if end >= 0:
                        i += end+2
                        inBlock = False
                        # print("now at:", i, row)
                    else:
                        i = len(row)
                else:
                    if row[i:i+2] == '/*':
                        inBlock = True
                        i += 2
                        # print("what now:", i)
                    elif row[i:i+2] == '//':
                        i = len(row)
                    else:
                        tmp += row[i]
                        i += 1
            if not inBlock and tmp != '':       # special case
                res += tmp,
            # print('res:', res)

        return res

print(Solution().removeComments(["a/*comment", "line", "more_comment*/b"])  # ab
# print(Solution().removeComments(["/*Test*//* program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
print(Solution().removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))

