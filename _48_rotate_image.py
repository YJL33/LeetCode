"""
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution(object):
    def rotate(self, A):
        """
        :type A: List[List[int]]
        :rtype: void Do not return anything, modify A in-place instead.
        """
        # clockwise rotate
        # first reverse upside down, and swap the symmetry 
        # 1 2 3     7 8 9     7 4 1
        # 4 5 6  => 4 5 6  => 8 5 2
        # 7 8 9     1 2 3     9 6 3
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]