/*
 11. Container With Most Water

    Total Accepted: 114060
    Total Submissions: 315610
    Difficulty: Medium
    Contributors: Admin

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
*/
# include <iostream>
# include <vector>

using std::vector;
using std::min;
using std::max;
using std::cout;
using std::endl;

class Solution {
 public:
    int maxArea(vector<int>& height) {
        int right = height.size()-1, left = 0, water = 0;
        while (right > left) {
            int h = std::min(height.at(right), height.at(left));
            int w = right - left;
            water = std::max(water, h*w);
            while (height.at(right) <= h && right > left) {
                right--;
            }
            while (height.at(left)<= h && right > left) {
                left++;
            }
        }
        return water;
    }
};
int main() {
    Solution sol = Solution();
    std::vector<int> inp = {1,2,4,3,2,5,6,7,2,34,1,32,2,3,5,1,9,1,2,1,16};
    std::cout << sol.maxArea(inp) << std::endl;
}