/*
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
*/
public class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        // Find where fast and slow meet
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while(slow != fast);
        int find = 0;
        // Find the entry of loop
        // can refer to http://codingfreak.blogspot.com/2012/12/detecting-first-node-in-a-loop.html
        while (find != slow) {
            slow = nums[slow];
            find = nums[find];
        }
        return find;
    }
}