"""
937. Reorder Data in Log Files

You have an array of logs.

Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.

Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier,
with the identifier used in case of ties.

The digit-logs should be put in their original order.

Return the final order of the logs.

 
Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.

Accepted 111.9K
Submissions 206.9K
"""
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # use identifier
        letterLogs = []
        digitLogs = []
        for l in logs:
            # insert with binary search
            if l[-1] not in "0123456789":
                k = 0
                while l[k] != " ": k += 1

                i, old = 0, len(letterLogs)
                while len(letterLogs) == old:
                    if old == 0 or old == i:
                        letterLogs += l,

                    j = 0
                    while letterLogs[i][j] != " ": j += 1

                    if letterLogs[i][j+1:] == l[k+1:] and letterLogs[i][:j+1] > l[:k+1]:
                        letterLogs.insert(i, l)
                    elif letterLogs[i][j+1:] > l[k+1:]:
                        letterLogs.insert(i, l)
                    else:
                        i += 1
            else:
                digitLogs += l,
        return letterLogs + digitLogs

print Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print Solution().reorderLogFiles(["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
print Solution().reorderLogFiles(["t kvr", "r 3 1", "i 403", "7 so", "t 54"])
print Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])
print Solution().reorderLogFiles(["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"])