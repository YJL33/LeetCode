/* Copyright [2017] <YJLee>
15. 3Sum

    Total Accepted: 181777
    Total Submissions: 862876
    Difficulty: Medium
    Contributors: Admin

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
# include <iostream>
# include <vector>
# include <algorithm>    // std::sort

using std::vector;
using std::sort;
using std::cout;
using std::endl;

class Solution {
 public:
    vector< vector<int> > threeSum(vector<int>& nums) {

        std::vector< std::vector<int> > res;
        if (nums.size() < 3) return res;

        std::sort (nums.begin(), nums.end());

        int last = nums.size()-1;
        for (int i = 0; i < nums.size()-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {    // here should compare with i-1
                continue;
            }
            if (nums[i] > 0 || (nums[i]+2*nums[last]) < 0) {    // too big / too small
            }
            int j = i+1, k = last;
            while (j < k) {

                if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                } else if (nums[i] + nums[j] + nums[k] < 0) {
                    j++;
                } else {

                    std::vector<int> tmp = {nums[i], nums[j], nums[k]};

                    res.push_back(tmp);
                    while (j+1 < k && nums[j] == nums[j+1]) {
                        j++;
                    }
                    while (j < k-1 && nums[k-1] == nums[k]) {
                        k--;
                    }
                    j++;
                    k--;
                }
            }
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    std::vector<int> test = {-1, 0, 1, 2, -1, -4};

    std::vector< std::vector<int> > ans = sol.threeSum(test);

    printf("Final Answer: \n");
    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            std::cout << ans[i][j] << ",";
        }
        std::cout << std::endl;
    }
}

