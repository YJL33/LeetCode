/*
26. Remove Duplicates from Sorted Array

Given a sorted array,
remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int i = 0;
        int j = 0;
        int L = nums.size();
        while (i+j < L-1) {
            if (nums[i] < nums[i+1]) {
                i++;
            }
            else {
                nums.erase(nums.begin() + i);   // Here uses "del" funciton, costs more time
                j++;
            }
        }
        return i+1;
    }
};
