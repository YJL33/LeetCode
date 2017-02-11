/* Copyright [2017] <YJLee>
 136. Single Number

    Total Accepted: 191187
    Total Submissions: 360705
    Difficulty: Easy
    Contributors: Admin

Given an array of integers,
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
*/
# include <iostream>
# include <vector>

using std::vector;
using std::cout;
using std::endl;

class Solution {
 public:
    int singleNumber(vector<int>& nums) {
        int ans = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            ans ^= nums[i];
        }
        return ans;
    }
};

int main() {
    std::vector<int> test;
    test.push_back(3);
    test.push_back(31);
    test.push_back(31);
    test.push_back(4);
    test.push_back(6);
    test.push_back(5);
    test.push_back(4);
    test.push_back(5);
    test.push_back(3);
    std::cout << Solution().singleNumber(test) << std::endl;
}