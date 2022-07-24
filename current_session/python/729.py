import sortedcontainers as sc
class MyCalendar:
    # clarification
    # inclusive? exclusive?
    # input validity? (e.g. start >= end)
    # upperbound/lowerbound of start/end time value? any negative? type?
    #
    # use sorted container
    # dummy case
    # e.g. [(10,20),(30,40),(2,5),(15,25),(16,36)]
    #
    # tc: O(logn) per book, O(nlogn) for n books
    # sc: O(n) for n books

    def __init__(self):
        self.starts = sc.SortedList()
        self.ends = sc.SortedList()

    def book(self, start: int, end: int) -> bool:
        # check whether it's valid to book
        # check the 'gap'
        # use bisect_left to find out the previous meeting span
        # idx-1 is the previous meeting span
        # idx is the next meeting span
        # make sure that previous_end <= start and end <= next_start
        idx = self.starts.bisect_left(start)
        # print('case: ', idx, self.starts, self.ends)
        if (idx-1 >= 0 and self.ends[idx-1] > start) or (idx < len(self.starts) and end > self.starts[idx]): return False

        self.starts.add(start)
        self.ends.add(end)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)