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
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    std::vector<int> twoSum(vector<int> &nums, int target) {
        // return: vector<int>
        std::unordered_map<int, int> dct;
        std::vector<int> res;
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
int main(int argc, const char * argv[])
{
    Solution sol = Solution();
    vector<int> a = {9,7,5,3,1};
    int b = 16;

    vector<int> res = sol.twoSum(a, b);
    for (int i=0; i < 2; i++)
    {
        cout << res[i] << endl;
    }
    return 0;
}