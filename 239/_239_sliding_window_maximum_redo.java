/*
239. Sliding Window Maximum

Given an array nums,
A sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

Hint:

How about using a data structure such as deque (double-ended queue)?
The queue size need not be the same as the window’s size.
Remove redundant elements and the queue should store only elements that need to be considered.
*/
import java.util.Arrays;
public class Solution {
    public int findLocalMax(int[] window) {
        int localmax = Integer.MIN_VALUE;
        for (int i : window) {
            if (i > localmax) localmax = i;
        }
        return localmax;
    }
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) return new int[0];      // special case
        int[] res = new int[nums.length-k+1];
        res[0] = findLocalMax(Arrays.copyOfRange(nums, 0, k));

        for (int j = k; j < nums.length; j++) {
            // if nums[j] is max => append it.
            if (nums[j] > res[j-k]) {
                res[j-k+1] = nums[j];
            }
            // if nums[j-k] is max => find a new one. (may use heap)
            else if (nums[j-k] == res[j-k]) {
                res[j-k+1] = findLocalMax(Arrays.copyOfRange(nums, j-k+1, j+1));
            }
            // if neither => just add last one again.
            else res[j-k+1] = res[j-k];
        }
        return res;
    }
}