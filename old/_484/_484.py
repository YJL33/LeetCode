"""
484. Find Permutation

    User Accepted: 182
    User Tried: 294
    Total Accepted: 188
    Total Submissions: 587
    Difficulty: Medium

By now, you are given a secret signature consisting of character 'D' and 'I'.
'D' represents a decreasing relationship between two numbers,
'I' represents an increasing relationship between two numbers.
And our secret signature was constructed by a special integer array,
which contains uniquely all the different number from 1 to n
(n is the length of the secret signature plus 1).
For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2],
but won't be constructed by array [3,2,4] or [2,1,3,4],
which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand,
now your job is to find the lexicographically smallest permutation of [1, 2, ... n]
could refer to the given secret signature in the input.

Example 1:

Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I",
where the number 1 and 2 construct an increasing relationship.

Example 2:

Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation,
you need to output [2,1,3]

Note:
The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
"""
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # if length of s = N, then we'll use 1 to N+1
        j, res = 0, [i+1 for i in range(len(s)+1)]
        # check the continual 'D' in s and reverse the corresponding part in res
        while j < len(s):
            if s[j] == 'I': j += 1
            else:
                head, tail = j, j
                while tail+1 < len(s) and s[tail+1] == 'D': tail += 1
                j = tail+1                      # move j to next position
                while tail+1 > head:            # reverse res[head:tail+2]
                    res[tail+1], res[head], head, tail = res[head], res[tail+1], head+1, tail-1
        return res

    def findPermutation2(self, s):
        head, tail, res = 0, 0, [i+1 for i in range(len(s)+1)]
        while tail < len(s):
            while tail+1 < len(s) and s[tail+1] == s[tail]: tail += 1
            # see it's 'I' or 'D'
            if s[head] == 'D': res[head:tail+2] = res[tail+1:head-1:-1] if head != 0 else res[tail+1::-1]
            head, tail = tail+1, tail+1
        return res