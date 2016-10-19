"""
 126. Word Ladder II

    Total Accepted: 54017
    Total Submissions: 395380
    Difficulty: Hard
    Contributors: Admin

Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the word list

For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:

    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""
import collections
class Solution(object):
    def findLadders(self, start, end, dic):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        dic.add(end)
        level = {start}                                 # record each visit
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:                          # for each visit
                for char in string.ascii_lowercase:
                    for i in range(len(start)):         # find each possible next step
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)                  # update visit record
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res