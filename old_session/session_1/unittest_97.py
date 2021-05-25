"""
unittest for Leetcode #97
"""
import unittest
import _97

class TestSolution(unittest.TestCase):

    def test_true2(self):
        s1 = ["ababdabdabdabab", "aabc"]
        s2 = ["acacacacacac", "abad"]
        s3 = ["abacabdacabadcabacdabacabac", "aabadabc"]
        map(self.assertTrue, map(_97.Solution().isInterleave, s1, s2, s3))
        map(self.assertTrue, map(_97.Solution().isInterleave2, s1, s2, s3))

    def test_false(self):
        s1 = ["aabcc", "bccd"]
        s2 = ["dbbca", "bbd"]
        s3 = ["aadbbbaccc", "cccdbbb"]
        map(self.assertFalse, map(_97.Solution().isInterleave1, s1, s2, s3))
        map(self.assertFalse, map(_97.Solution().isInterleave2, s1, s2, s3))

if __name__ == "__main__":
    unittest.main()