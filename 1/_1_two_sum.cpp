/*
1. Two Sum

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
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // return: vector<int>
        unordered_map<int, int> dct;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            int x = nums[i];
            if (dct.find(target-x) != dct.end()) {      // find it in dct
                res.push_back(dct[target-x]);
                res.push_back(i);
                return res;
            }
            dct[x] = i;
        }
        return res;
    }
};
