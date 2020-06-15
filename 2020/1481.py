"""
5437. Least Number of Unique Integers after K Removals
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium

Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # use collections
        numCount = {}
        for n in arr:
            if n not in numCount:
                numCount[n] = 1
            else:
                numCount[n] += 1

        count = []
        for key in numCount.keys():
            count += numCount[key],

        count.sort()

        i = 0
        while i < len(count) and k-count[i] >= 0:
            k -= count[i]
            i += 1

        return len(count) - i


