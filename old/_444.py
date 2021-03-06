"""
444. Sequence Reconstruction

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 <= n <= 104.
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].

Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
"""
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # O(N^2) N = len(org), make seqs as dictionary still TLE
        # should fix number of constraints
        if (org and not seqs) or (not org and seqs): return False
        constraints = sum([len(s)*(len(s)-1)/2 for s in seqs if s])
        if len(org) == 1:                                 # corner case
            for s in seqs:
                if not s or len(s) != 1 or s[0] != org[0]:
                    return False
            return True

        elif len(org)-1 > constraints: return False      # Not enough comparements

        flags = [None for _ in xrange(len(org))]

        seqdct = []
        for s in seqs:
            seqdct += {},
            for i in xrange(len(s)):
                seqdct[-1][s[i]] = i

        for i in xrange(len(org)-1):
            for j in xrange(i+1, len(org)):
                a, b = org[i], org[j]
                for k in xrange(len(seqdct)):
                    if a in seqdct[k] and b in seqdct[k]:
                        if seqdct[k][a] < seqdct[k][b]:
                            flags[i] = True
                        else:
                            flags[i] = False            # definitely wrong
                            break
            if not flags[i] or flags[i] == None:
                return False

        return True
