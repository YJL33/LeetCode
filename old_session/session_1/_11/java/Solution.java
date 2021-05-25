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
import java.util.*;

public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length-1, water = 0;
        while (right > left) {
            int h = Math.min(height[left], height[right]);
            int w = right-left;
            water = Math.max(water, h*w);
            while (left < right && height[left] <= h) {
                left++;
            }
            while (left < right && height[right] <= h) {
                right--;
            }
        }
        return water;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] inp = {1,2,4,3,2,5,6,7,2,34,1,32,2,3,5,1,9,1,2,1,16};
        System.out.println(sol.maxArea(inp));
    }
}