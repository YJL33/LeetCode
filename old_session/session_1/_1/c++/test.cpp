
//  test

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <unordered_map>

#include "_1_two_sum.h"

using namespace std;

std::vector<int> twoSum(vector<int> &nums, int target);

int main(int argc, const char * argv[])
{
    cout << "Two sum: [9,7,5,3,1], 16" << endl;
    std::vector<int> nums = {9,7,5,3,1};
    int tgt = 16;
    vector<int> res = twoSum(nums, tgt);
    for (int i=0;i < 2;i++) {
        std::cout << ' ' << res[i];
    }
    //printf("Size of Law's filter: %d, Size of image: %d x %d", (WindowSize*WindowSize), Size, Size);
    return 0;
}