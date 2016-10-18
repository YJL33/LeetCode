import unittest
import _164

class TestSolution(unittest.TestCase):
    def test_none_0(self):
        s = [1,7,3,3]
        s2 = [3,5,8,9,6,2,1,4,7,10,100,1000,1500,20,30,40,50,60,80,70,90,100]
        s3 = [1,10000000]
        s4 = [1,10000001]
        self.assertTrue(_164.Solution().maximumGap(s) == 4)
        self.assertTrue(_164.Solution().maximumGap(s2) == 900)
        self.assertTrue(_164.Solution().maximumGap(s3) == (10000000-1))
        self.assertTrue(_164.Solution().maximumGap(s4) == (10000000))

if __name__ == "__main__":
    unittest.main()