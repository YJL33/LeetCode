"""
Dictionaries in python:
https://goo.gl/2vWop5
"""
class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for i in range(len(A)):
            if A[i] not in dict:
                dict[A[i]] = 1
            else:
                dict[A[i]] += 1
        for word in dict:
            if dict[word] == 1:
                return word