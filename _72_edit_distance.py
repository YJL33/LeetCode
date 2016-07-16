"""
72. Edit Distance

Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # From word1 -> word2
        if len(word1) == 0:
            return len(word2)

        # minDistance(word1, word2) should be equal to minDistance(word2, word1)
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        # Now len(word1) >= len(word2)
        #print "from ", word1, "to ", word2
        prev_dist = range(len(word2) + 1)   # prev_dist[j+1]: distance from word1 to word2[j]
                                            # initially, prev_dist[j] should be j
        for i, c1 in enumerate(word1):
            current_dist = [i + 1]
            for j, c2 in enumerate(word2):
                #print word1[:min(i+1, len(word1))], "from ", word1, " <=> ", word2[:min(j+1, len(word2))], "from ", word2
                insert = prev_dist[j+1] + 1     # j+1 instead of j since prev_dist and current_dist
                delete = current_dist[j] + 1    # are one character longer than word2
                replace = prev_dist[j] + (c1 != c2)
                current_dist.append(min(insert, delete, replace))
                #print "picking...", insert, delete, replace
            prev_dist = current_dist
            #print "current distance: ", current_dist[1:], "(from ", word1[:min(i+1, len(word1))], "to ", word2, ")"
        
        return prev_dist[-1]
