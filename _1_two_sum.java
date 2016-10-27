/*
1. Two Sum

    Total Accepted: 318702
    Total Submissions: 1164679
    Difficulty: Easy

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices.
Please read the above updated description carefully.
*/
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> numdict = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numdict.containsKey(target - nums[i])) {    // got it
                res[1] = i;                                 // index of b
                res[0] = numdict.get(target - nums[i]);     // index of a
                return res;
            }
            numdict.put(nums[i], i);        // put seen number into hashmap
        }
        return res;
    }
}