import unittest
import _65

class TestSolution(unittest.TestCase):
    def test_true(self):
        s = '0'
        s2 = ' 0.1'
        s3 = '0.e4'
        s7 = '+96'
        s8 = '-5'
        self.assertTrue(_65.Solution().isNumber(s))
        self.assertTrue(_65.Solution().isNumber(s2))
        self.assertTrue(_65.Solution().isNumber(s3))
        self.assertTrue(_65.Solution().isNumber(s7))
        self.assertTrue(_65.Solution().isNumber(s8))
    def test_true2(self):
        sd = '.5'
        se = '9.'
        sh = '4e+4'
        si = '8e-1'
        self.assertTrue(_65.Solution().isNumber(sd))
        self.assertTrue(_65.Solution().isNumber(se))
        self.assertTrue(_65.Solution().isNumber(sh))
        self.assertTrue(_65.Solution().isNumber(si))
    def test_false(self):
        s4 = 'abc'
        s5 = '0. 2'
        s6 = '  10e33e4  '
        s9 = '9 8 7 6 5'
        self.assertFalse(_65.Solution().isNumber(s4))
        self.assertFalse(_65.Solution().isNumber(s5))
        self.assertFalse(_65.Solution().isNumber(s6))
        self.assertFalse(_65.Solution().isNumber(s9))
    def test_false2(self):
        sa = '+   8'
        sb = '. '
        sc = '14-'
        sf = '4e+'
        sg = '6e6.5'
        self.assertFalse(_65.Solution().isNumber(sa))
        self.assertFalse(_65.Solution().isNumber(sb))
        self.assertFalse(_65.Solution().isNumber(sc))
        self.assertFalse(_65.Solution().isNumber(sf))
        self.assertFalse(_65.Solution().isNumber(sg))

if __name__ == "__main__":
    unittest.main()