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
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int [] ans = new int[nums.length-k+1];
        if (nums.length == 0) return new int[0];
        int cur = 0;
        int localmax = Integer.MIN_VALUE;
        for (int i = 0; i < k; ++i) {
            if (nums[i] > localmax) { localmax = nums[i]; }
        }
        ans[cur] = localmax;
        for (int i = k; i < nums.length; ++i) {
            // if latest one is maximum => add it
            if (nums[i] >= ans[i-k]) {
                localmax = nums[i];
                ans[++cur] = localmax;
            }
            // if oldest one is maximum => find a new one.
            else if (nums[i-k] == ans[i-k]) {
                localmax = Integer.MIN_VALUE;
                for (int j = i-k+1; j < i+1; ++j) {
                    if (nums[j] >= localmax) { localmax = nums[j]; }
                }
                ans[++cur] = localmax;
            }
            // if neither => add the last one
            else {
                ans[++cur] = localmax;
            }
        }
        return ans;
    }
}