"""
 277. Find the Celebrity

    Total Accepted: 18749
    Total Submissions: 52929
    Difficulty: Medium
    Contributors: Admin

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,
there may exist one celebrity.
The definition of a celebrity is:
all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like:
"Hi, A. Do you know B?" to get information of whether A knows B.
You need to find out the celebrity (or verify there is none) by asking as few questions as possible
(in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B.
Implement a function int findCelebrity(n),
your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.
"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in xrange(n):          # ask x know i or not
            if knows(x, i): x = i    # now assign i to x, the potential celebrity (knowing no one).
        if any(knows(x, i) for i in xrange(x)): return -1
        if any(not knows(i, x) for i in xrange(n)): return -1
        return x
