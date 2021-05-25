"""
unittest for #56
"""
import unittest
import _56_merge_intervals as _56

class TestSolution(unittest.TestCase):
    def test_true(self):
        s = [[1,3],[2,6],[8,10],[15,18]]
        t = map(_56.Interval, [c[0] for c in s], [c[1] for c in s])

        print [(c.start, c.end) for c in _56.Solution().merge(t)]

        #self.assertTrue(_56.Solution().merge(t))

if __name__ == "__main__":
    unittest.main()