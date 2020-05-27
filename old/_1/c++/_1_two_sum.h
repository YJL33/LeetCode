/*
1. Two Sum
*/
#ifndef _1_two_sum
#define _1_two_sum

#include <stdio.h>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:

    std::vector<int> twoSum(vector<int>& nums, int target) {
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

#endif /* defined(_1_two_sum) */

