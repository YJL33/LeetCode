
import unittest
#import _10_regular_expression_matching as mod10
import _44 as mod44

class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(mod44.Solution().isMatch(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(mod44.Solution().isMatch(s, p))

    def test_no_symbol_equal(self):
        s = "abcde"
        p = "abcd?"
        self.assertTrue(mod44.Solution().isMatch(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(mod44.Solution().isMatch(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "ab?"
        self.assertFalse(mod44.Solution().isMatch(s, p))

    def test_symbol_0(self):
        s = "aaaaaaaaa"
        p = "*"
        self.assertTrue(mod44.Solution().isMatch(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertFalse(mod44.Solution().isMatch(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(mod44.Solution().isMatch(s, p))


if __name__ == "__main__":
    unittest.main()