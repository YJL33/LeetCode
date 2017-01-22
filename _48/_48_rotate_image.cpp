/*
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/
#include <stdio.h>      /* printf */
#include <utility>      // std::swap, std::reverse
class Solution {
public:
    void rotate(vector<vector<int>>& image) {
        /*
        clockwise rotate
        first reverse up to down, then swap the symmetry 
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        */
        std::reverse(image.begin(),image.end());
        for (int i = 0; i < image.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                std::swap(image[i][j], image[j][i]);
            }
        }
    }
};