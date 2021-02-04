class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        
        # use binary search
        def bs(l, r):
            # find first
            while l < r:
                m = l + (r-l)/2
                if nums[m] >= target:    # in the left side
                    r = m
                else:
                    l = m+1
            return l
        
        def bs2(l, r):
            # find last
            while l < r:
                m = l + (r-l)/2
                if nums[m] > target:
                    r = m
                else:
                    l = m+1
            return l
        
        l, r = 0, len(nums)-1
        first = bs(l, r)
        
        # this is where 'target' should be inserted
        # check nums[l] == target or not
        if nums[first] != target:
            return [-1,-1]
        else:
            # find last
            last = bs2(first, r)
            if last > len(nums)-1 or nums[last] != target:
                last -= 1
            return [first, last]