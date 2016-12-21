"""
 451. Sort Characters By Frequency

    Total Accepted: 9065
    Total Submissions: 18057
    Difficulty: Medium
    Contributors: stickypens

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # for each char, put it into a dictionary
        worddct = {}
        for c in s:
            if c in worddct:
                worddct[c] += 1
            else:
                worddct[c] = 1
        minheap = []
        for k, v in worddct.iteritems():
            heapq.heappush(minheap, ((-1)*v, k))
        ans = ""
        while len(minheap) > 0:
            cnt, char = heapq.heappop(minheap)
            ans += char*((-1)*cnt)
        return ans