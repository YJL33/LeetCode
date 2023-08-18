#include <iostream>
#include <vector>

using namespace std;

// cp c++/189.cpp c++/sol.cpp && clang++ -std=c++17 c++/189.cpp -o sol && ./sol -v 
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // pop front and push back (L-k) times
        // TC: O(L)*(L-k)
        // SC: O(1)
        // use additional array - copy
        // TC: O(L)
        // SC: O(L)
        int L = nums.size();
        k = k%L;
        int arr[L];
        copy(nums.begin(), nums.end(), arr);
        // assign the new array from left to right
        // diff = L-k
        for (int i=0; i<L; i++) {
            nums[i] = arr[(i+L-k)%L];
        }
        return;
    }
};